"""
PC-DMIS 版本:
                    2018 R1
                    2019 R2
                    2023.2
                    
"""
from customexception import CustomException
from dialog import Dialog
import constants
from topmessagebox import TopMessagebox
from pcdlrnconst.pcdlrnconst20232 import constants as pdconst

import win32com.client as wc
import hashlib
# import re
# import importlib
import os
from types import MethodType
from enum import Enum, auto
import pywintypes

Dialog()

class PcdmisTools:
    app = None
    part = None
    cmds = None
    showNegative: bool = None
    # pdconst = None
    pivotVersion = '2022'
    getFcfFromCmd: MethodType = None

    # @staticmethod
    # def importPcdlrnConst(version: str):
    #     packageName = 'pcdlrnconst'
    #     moduleName = packageName + '.' + packageName + re.sub(r'[ .]', '', version)
    #     try:
    #         PcdmisTools.pdconst = importlib.import_module(moduleName, packageName).constants
    #     except ModuleNotFoundError:
    #         raise ValueError(f'未找到 {version} 版本的模块')
        
    @staticmethod
    def initPcdlrnTools(version: str):
        if version >= PcdmisTools.pivotVersion:
            # PcdmisTools.importPcdlrnConst('2023.2')
            PcdmisTools.getFcfFromCmd = PcdmisTools.getFcfFromCmd20232
        else:
            # PcdmisTools.importPcdlrnConst('2019 R2')
            PcdmisTools.getFcfFromCmd = PcdmisTools.getFcfFromCmd2019R2

    @staticmethod
    def connect(online: bool = True) -> tuple[str, str]:
        """
        连接 PC-DMIS

        Args:
            online (bool): 是否连接联机程序，否则连接前台程序

        Returns:
            (PC-DMIS 版本, 当前程序名称)
        """
        if PcdmisTools.app is not None:
            Dialog.log('PC-DMIS 已经连接')
        else:
            try:
                PcdmisTools.app = wc.Dispatch('PCDLRN.Application')
            except pywintypes.com_error as e:
                if e.hresult == -2147221021 or e.hresult == -2146959355:
                    msg = '请确保PC-DMIS已经以管理员身份运行'
                    TopMessagebox.show('错误', msg, TopMessagebox.ERROR)
                    raise CustomException(msg, CustomException.ERROR)
                else:
                    raise CustomException('连接 PC-DMIS 失败', CustomException.ERROR)
            Dialog.log(f'连接 PC-DMIS 成功，版本：{PcdmisTools.app.VersionString}')

        PcdmisTools.part = None
        count = 1
        programString = ''
        # 获取所有测量程序
        parts = PcdmisTools.app.PartPrograms

        if online:
            for part in parts:
                programName = part.Name
                machine = part.ActiveMachine
                status = machine.ConnectionStatus
                programString += f'({count}) 测量程序名：{programName}，设备：{machine}，连接状态：'
                match status:
                    case pdconst.NotAvailable:
                        programString += '不可用'
                    case pdconst.MachineNotConnected:
                        programString += '未连接'
                    case pdconst.MachineHoming:
                        programString += '正在回零'
                    case pdconst.MachineDisconnecting:
                        programString += '正在断开连接'
                    case pdconst.MachineConnecting:
                        programString += '正在连接'
                    case pdconst.MachineConnected:
                        PcdmisTools.part = part
                        programString += '已连接'
                programString += '；'
                count += 1
            Dialog.log(f'已打开程序数：{parts.Count}，程序状态：{programString}')

        if PcdmisTools.part is None:
            Dialog.log('尝试获取当前前台的程序')
            PcdmisTools.part = PcdmisTools.app.ActivePartProgram
        
        if PcdmisTools.part is None:
            raise CustomException('获取程序失败', CustomException.CRITICAL)
        else:
            Dialog.log(f'连接 PC-DMIS 程序成功，程序名：{PcdmisTools.part.Name}')
            PcdmisTools.initPcdlrnTools(PcdmisTools.app.VersionString)
            PcdmisTools.showNegative = PcdmisTools.part.PartProgramSettings.MinusTolerancesShowNegative
        PcdmisTools.cmds = PcdmisTools.part.Commands

        return PcdmisTools.app.VersionString, PcdmisTools.part.Name
    
    data = {
        '命令名': None,
        '特征': None,
        '轴': None,
        '单位': None,
        '标称值': None,
        '上公差': None,
        '下公差': None,
        '上限值': None,
        '下限值': None,
        '实测值': None,
        '补偿值': None,
        '类型': None
    }

    class dataType(Enum):
        DIMENSION = auto()
        FCF = auto()
        FCFDIM = auto()

    dataKeys = list(data.keys())
    dataLen = len(dataKeys)

    @staticmethod
    def clearData():
        PcdmisTools.data = {key: None for key in PcdmisTools.data.keys()}

    @staticmethod
    def getDimensionFromCmd(idx, cmd, precision) -> list[dict]:
        """
        从测量命令对象中获取尺寸数据

        Params:
            cmd: 测量命令对象
            precision: 浮点数精度

        Returns:
            list[dict]
        """
        if not cmd.isDimension:
            return None, idx

        dim = cmd.DimensionCommand
        if dim is None:
            Dialog.log('获取尺寸对象失败', Dialog.WARNING)
            return None, idx
        
        datas = []
        measured = cmd.GetFieldValue(pdconst.DIM_MEASURED, 0)
        if measured != False: # 排除形位公差和基准
            PcdmisTools.clearData()
            PcdmisTools.data['命令名'] = dim.ID
            PcdmisTools.data['特征'] = dim.Feat1 + ' ' + dim.Feat2 + ' ' + dim.Feat3
            PcdmisTools.data['单位'] = cmd.GetFieldValue(pdconst.UNIT_TYPE, 0)
            if cmd.GetFieldValue(pdconst.AXIS, 0) == False and PcdmisTools.cmds[idx + 1].ID == '': # 这是一个位置命令，继续下一条命令
                idx += 1
                cmd = PcdmisTools.cmds[idx]
                dim = cmd.DimensionCommand
            PcdmisTools.data['轴'] = dim.AxisLetter
            PcdmisTools.data['标称值'] = round(dim.NOMINAL, precision)
            PcdmisTools.data['上公差'] = round(dim.Plus, precision)
            PcdmisTools.data['下公差'] = -round(dim.Minus, precision) # 下公差默认正数表示负数，用负数表示正数
            PcdmisTools.data['上限值'] = round(dim.NOMINAL + dim.Plus, precision)
            PcdmisTools.data['下限值'] = round(dim.NOMINAL - dim.Minus, precision)
            PcdmisTools.data['实测值'] = round(dim.Measured, precision)
            PcdmisTools.data['补偿值'] = round(dim.Bonus, precision)
            PcdmisTools.data['类型'] = PcdmisTools.dataType.DIMENSION

            Dialog.log(f'读取到：{PcdmisTools.data}')
            datas.append(PcdmisTools.data.copy())
        return datas, idx
    
    @staticmethod
    def getFcfFromCmd2019R2(idx, cmd, precision) -> list[dict]:
        """
        从测量命令对象中获取形位公差数据

        Params:
            cmd: 测量命令对象
            precision: 浮点数精度

        Returns:
            list[dict]
        """
        if not cmd.isFCFCommand:
            return None, idx
        
        datas = []

        # 形位公差评价对象自身的尺寸信息
        for i in range(1, cmd.GetDataTypeCount(pdconst.LINE1_MEAS) + 1):
            PcdmisTools.clearData()
            PcdmisTools.data['单位'] = cmd.GetFieldValue(pdconst.UNIT_TYPE, 0)
            PcdmisTools.data['命令名'] = cmd.GetFieldValue(pdconst.LINE1_TBLHDR, i)
            PcdmisTools.data['特征'] = cmd.GetFieldValue(pdconst.LINE1_FEATNAME, i)
            PcdmisTools.data['轴'] = None

            nominal = cmd.GetFieldValue(pdconst.LINE1_NOMINAL, i)
            PcdmisTools.data['标称值'] = round(nominal, precision)
            plus = cmd.GetFieldValue(pdconst.LINE1_PLUSTOL, i)
            PcdmisTools.data['上公差'] = round(plus, precision)
            minustol = cmd.GetFieldValue(pdconst.LINE1_MINUSTOL, i)
            if not PcdmisTools.showNegative:
                minustol = -minustol
            PcdmisTools.data['下公差'] = round(minustol, precision)
            PcdmisTools.data['上限值'] = round(nominal + plus, precision)
            PcdmisTools.data['下限值'] = round(nominal + minustol, precision)
            meas = cmd.GetFieldValue(pdconst.LINE1_MEAS, i)
            PcdmisTools.data['实测值'] = round(meas, precision)
            bonus = cmd.GetFieldValue(pdconst.LINE1_BONUS, i)
            PcdmisTools.data['补偿值'] = round(bonus, precision)
            PcdmisTools.data['类型'] = PcdmisTools.dataType.FCFDIM

            Dialog.log(f'读取到：{PcdmisTools.data}')
            datas.append(PcdmisTools.data.copy())

        # 形位公差
        for i in range(1, cmd.GetDataTypeCount(pdconst.LINE2_MEAS) + 1):
            PcdmisTools.clearData()
            PcdmisTools.data['单位'] = cmd.GetFieldValue(pdconst.UNIT_TYPE, 0)

            runoutType = cmd.GetFieldValue(pdconst.FCF_RUNOUT_TYPE, i)
            if runoutType == False:
                runoutType = ''
            else:
                runoutType = ' - ' + runoutType

            PcdmisTools.data['命令名'] = cmd.GetFieldValue(pdconst.LINE2_TBLHDR, i) + runoutType
            PcdmisTools.data['特征'] = cmd.GetFieldValue(pdconst.LINE2_FEATNAME, i)
            PcdmisTools.data['轴'] = cmd.GetFieldValue(pdconst.LINE2_AXIS, i)

            nominal = cmd.GetFieldValue(pdconst.LINE2_NOMINAL, i)
            PcdmisTools.data['标称值'] = round(nominal, precision)
            plus = cmd.GetFieldValue(pdconst.LINE2_PLUSTOL, i)
            PcdmisTools.data['上公差'] = round(plus, precision)
            minustol = cmd.GetFieldValue(pdconst.LINE2_MINUSTOL, i)
            PcdmisTools.data['上限值'] = PcdmisTools.data['上公差']
            meas = cmd.GetFieldValue(pdconst.LINE2_MEAS, i)
            PcdmisTools.data['实测值'] = round(meas, precision)
            bonus = cmd.GetFieldValue(pdconst.LINE2_BONUS, i)
            PcdmisTools.data['补偿值'] = round(bonus, precision)
            PcdmisTools.data['类型'] = PcdmisTools.dataType.FCF

            Dialog.log(f'读取到：{PcdmisTools.data}')
            datas.append(PcdmisTools.data.copy())

        return datas, idx

    @staticmethod
    def getFcfFromCmd20232(idx, cmd, precision) -> list[dict]:
        """
        从测量命令对象中获取形位公差数据

        Params:
            cmd: 测量命令对象
            precision: 浮点数精度

        Returns:
            list[dict]
        """
        if not cmd.IsToleranceCommand:
            return None, idx
        tolCmd = cmd.ToleranceCommand

        datas = []

        # 形位公差评价对象自身的尺寸信息
        for i in range(1, tolCmd.sizeCountCombined + 1):
            PcdmisTools.clearData()
            PcdmisTools.data['命令名'] = tolCmd.ID + ' 尺寸'
            PcdmisTools.data['特征'] = tolCmd.sizeText(i)
            PcdmisTools.data['轴'] = tolCmd.SizeAxis(i)
            PcdmisTools.data['单位'] = tolCmd.ReportUnits
            PcdmisTools.data['标称值'] = round(tolCmd.sizeNominal(i), precision)
            PcdmisTools.data['上公差'] = round(tolCmd.sizePlusTol(i), precision)
            sizeNibusTol = tolCmd.sizeMinusTol(i)
            if not PcdmisTools.showNegative:
                sizeNibusTol = -sizeNibusTol
            PcdmisTools.data['下公差'] = round(sizeNibusTol, precision)
            PcdmisTools.data['上限值'] = round(tolCmd.sizeNominal(i) + tolCmd.sizePlusTol(i), precision)
            PcdmisTools.data['下限值'] = round(tolCmd.sizeNominal(i) + sizeNibusTol, precision)

            PcdmisTools.data['实测值'] = round(tolCmd.sizeMeasured(i), precision)
            PcdmisTools.data['类型'] = PcdmisTools.dataType.FCFDIM

            Dialog.log(f'读取到：{PcdmisTools.data}')
            datas.append(PcdmisTools.data.copy())

        # 形位公差
        for i in range(1, tolCmd.SegmentCount + 1):
            for j in range(1, tolCmd.FeatureCount + 1):
                PcdmisTools.clearData()
                PcdmisTools.data['命令名'] = tolCmd.ID
                PcdmisTools.data['特征'] = tolCmd.FeatureID(j)
                PcdmisTools.data['轴'] = tolCmd.SegmentAxis(j)
                PcdmisTools.data['单位'] = tolCmd.ReportUnits
                PcdmisTools.data['标称值'] = round(tolCmd.segmentDimNominal(i, j), precision)
                PcdmisTools.data['上公差'] = round(tolCmd.segmentDimPlusTol(i, j), precision)
                PcdmisTools.data['上限值'] = PcdmisTools.data['上公差']
                PcdmisTools.data['实测值'] = round(tolCmd.segmentDimMeasured(i, j), precision)
                PcdmisTools.data['补偿值'] = round(tolCmd.SegmentDimBonus(i, j), precision)
                PcdmisTools.data['类型'] = PcdmisTools.dataType.FCF

                Dialog.log(f'读取到：{PcdmisTools.data}')
                datas.append(PcdmisTools.data.copy())

        return datas, idx

    @staticmethod
    def getData() -> tuple[str, list[dict]]:
        """
        获取尺寸和形位公差数据

        Returns:
            (序列号, list[dict])
        """
        if PcdmisTools.cmds is None:
            raise CustomException('请先连接 PC-DMIS 程序后，再获取数据', CustomException.WARNING)
        
        dataList = []
        idx = 0
        while idx < PcdmisTools.cmds.Count:
            cmd = PcdmisTools.cmds[idx]
            dimensionData, idx = PcdmisTools.getDimensionFromCmd(idx, cmd, constants.Data.precision)
            if dimensionData is not None:
                dataList += dimensionData
            fcfDatas, idx = PcdmisTools.getFcfFromCmd(idx, cmd, constants.Data.precision)
            if fcfDatas is not None:
                dataList += fcfDatas
            idx += 1

        serialNumber = PcdmisTools.part.SerialNumber

        return serialNumber, dataList
    
    @staticmethod
    def calcDigest(dataList: list[dict]) -> str:
        """
        计算测量项目的摘要

        Params:
            dataList: 测量数据

        Returns:
            返回摘要的十六进制字符串（64位）
        """
        if len(dataList) == 0:
            raise CustomException('数据为空', CustomException.ERROR)
        sumaryString = ''
        for data in dataList:
            for key, value in data.items():
                if key in ['上限值', '下限值', '补偿值', '实测值']:
                    continue
                sumaryString += f'{value}'
        Dialog.log(f'特征字符串：{sumaryString}')
        return hashlib.sha256(sumaryString.encode('utf-8')).hexdigest()
    
    @staticmethod
    def removeExternalCommand():
        """
        移除使用本工具的外部命令
        """
        if PcdmisTools.cmds is None:
            Dialog.log('请先连接 PC-DMIS 程序后，再使用移除命令', Dialog.WARNING)
            return
        idx = PcdmisTools.cmds.Count - 1
        while idx > 0 :
            cmd = PcdmisTools.cmds[idx]
            if cmd.IsExternalCommand:
                extCmdStr = cmd.GetFieldValue(pdconst.COMMAND_STRING, 0)
                if 'pcdmis-export-data' in extCmdStr:
                    cmd.Remove()
                    Dialog.log(f'删除外部命令：{extCmdStr}')
            idx -= 1

    @staticmethod
    def addExternalCommand(exePath: str):
        """
        添加外部命令

        Params:
            exePath: 外部命令的路径
        """
        if PcdmisTools.cmds is None:
            Dialog.log('请先连接 PC-DMIS 程序后，再添加命令', Dialog.WARNING)
            return
        
        # 获取最后一条命令
        cmdNumber = PcdmisTools.cmds.Count
        endCmd = PcdmisTools.cmds[cmdNumber - 1]

        # 将插入点设置到最后一条命令之后
        PcdmisTools.cmds.InsertionPointAfter(endCmd)

        cmd = PcdmisTools.cmds.Add(pdconst.EXTERNAL_COMMAND, True)
        cmd.PutText(exePath, pdconst.COMMAND_STRING, 0)
        cmd.PutText('不显示', pdconst.DISPLAY_TRACE, 0)
        cmd.PutText('等待', pdconst.TRACE_NAME, 0)

        Dialog.log(f'添加外部命令：{exePath}')

    def getCurProgPath():
        """
        获取当前测量程序的绝对路径
        """
        return PcdmisTools.part.FullName

    def saveProg():
        """
        保存测量程序

        Returns:
            保存成功返回 True，否则返回 False
        """
        if PcdmisTools.part is None:
            raise CustomException('请先连接 PC-DMIS 程序后，再保存程序', CustomException.WARNING)

        if PcdmisTools.part.Save:
            Dialog.log(f'保存测量程序成功：{PcdmisTools.getCurProgPath()}')
            return True
        else:
            Dialog.log(f'保存测量程序失败：{PcdmisTools.getCurProgPath()}')
            return False
        
def test1():
    """基本功能测试"""
    version, program = PcdmisTools.connect()
    print(f'PC-DMIS 版本：{version}，程序名：{program}')

    dataKey = PcdmisTools.dataKeys
    dataLen = PcdmisTools.dataLen
    print(f'数据键： {dataKey}, 个数：{dataLen}')

    serialNumber, dataList = PcdmisTools.getData()
    print(f'序列号：{serialNumber}')
    for data in dataList:
        print(data)

    digest = PcdmisTools.calcDigest(dataList)
    print(digest)

if __name__ == '__main__':
    test1()