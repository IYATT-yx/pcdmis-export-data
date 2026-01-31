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
            (PC-DMIS 版本, 当前程序名称, 程序完整路径)
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

        return PcdmisTools.app.VersionString, PcdmisTools.part.Name, PcdmisTools.part.FullName
    
    dataTemplate = {
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

    dataKeys = list(dataTemplate.keys())
    dataLen = len(dataKeys)

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
        
        data = PcdmisTools.dataTemplate.copy()
        datas = []
        measured = cmd.GetFieldValue(pdconst.DIM_MEASURED, 0)
        if measured != False: # 排除形位公差和基准
            data['命令名'] = dim.ID
            data['特征'] = dim.Feat1 + ' ' + dim.Feat2 + ' ' + dim.Feat3
            data['单位'] = cmd.GetFieldValue(pdconst.UNIT_TYPE, 0)
            if cmd.GetFieldValue(pdconst.AXIS, 0) == False and PcdmisTools.cmds[idx + 1].ID == '': # 这是一个位置命令，继续下一条命令
                idx += 1
                cmd = PcdmisTools.cmds[idx]
                dim = cmd.DimensionCommand

            nominal = dim.NOMINAL
            plus = dim.Plus
            minus = dim.Minus

            data['轴'] = dim.AxisLetter
            data['标称值'] = round(nominal, precision)
            data['上公差'] = round(plus, precision)
            data['下公差'] = -round(minus, precision) # 下公差默认正数表示负数，用负数表示正数
            data['上限值'] = round(nominal + plus, precision)
            data['下限值'] = round(nominal - minus, precision)
            data['实测值'] = round(dim.Measured, precision)
            data['补偿值'] = round(dim.Bonus, precision)
            data['类型'] = PcdmisTools.dataType.DIMENSION

            datas.append(data)
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
            data = PcdmisTools.dataTemplate.copy()
            data['单位'] = cmd.GetFieldValue(pdconst.UNIT_TYPE, 0)
            data['命令名'] = cmd.GetFieldValue(pdconst.LINE1_TBLHDR, i)
            data['特征'] = cmd.GetFieldValue(pdconst.LINE1_FEATNAME, i)
            data['轴'] = None

            nominal = cmd.GetFieldValue(pdconst.LINE1_NOMINAL, i)
            data['标称值'] = round(nominal, precision)
            plus = cmd.GetFieldValue(pdconst.LINE1_PLUSTOL, i)
            data['上公差'] = round(plus, precision)
            minustol = cmd.GetFieldValue(pdconst.LINE1_MINUSTOL, i)
            if not PcdmisTools.showNegative:
                minustol = -minustol
            data['下公差'] = round(minustol, precision)
            data['上限值'] = round(nominal + plus, precision)
            data['下限值'] = round(nominal + minustol, precision)
            meas = cmd.GetFieldValue(pdconst.LINE1_MEAS, i)
            data['实测值'] = round(meas, precision)
            bonus = cmd.GetFieldValue(pdconst.LINE1_BONUS, i)
            data['补偿值'] = round(bonus, precision)
            data['类型'] = PcdmisTools.dataType.FCFDIM

            datas.append(data)

        # 形位公差
        for i in range(1, cmd.GetDataTypeCount(pdconst.LINE2_MEAS) + 1):
            data = PcdmisTools.dataTemplate.copy()
            data['单位'] = cmd.GetFieldValue(pdconst.UNIT_TYPE, 0)

            runoutType = cmd.GetFieldValue(pdconst.FCF_RUNOUT_TYPE, i)
            if runoutType == False:
                runoutType = ''
            else:
                runoutType = ' - ' + runoutType

            data['命令名'] = cmd.GetFieldValue(pdconst.LINE2_TBLHDR, i) + runoutType
            data['特征'] = cmd.GetFieldValue(pdconst.LINE2_FEATNAME, i)
            data['轴'] = cmd.GetFieldValue(pdconst.LINE2_AXIS, i)

            nominal = cmd.GetFieldValue(pdconst.LINE2_NOMINAL, i)
            data['标称值'] = round(nominal, precision)
            plus = cmd.GetFieldValue(pdconst.LINE2_PLUSTOL, i)
            data['上公差'] = round(plus, precision)
            minustol = cmd.GetFieldValue(pdconst.LINE2_MINUSTOL, i)
            data['上限值'] = data['上公差']
            meas = cmd.GetFieldValue(pdconst.LINE2_MEAS, i)
            data['实测值'] = round(meas, precision)
            bonus = cmd.GetFieldValue(pdconst.LINE2_BONUS, i)
            data['补偿值'] = round(bonus, precision)
            data['类型'] = PcdmisTools.dataType.FCF

            datas.append(data)

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

        id = tolCmd.ID
        sizeText = tolCmd.sizeText
        sizeAxis = tolCmd.SizeAxis
        reportUnits = tolCmd.ReportUnits
        sizeNominal = tolCmd.sizeNominal
        sizePlusTol = tolCmd.sizePlusTol
        sizeMinusTol = tolCmd.sizeMinusTol
        sizeMeasured = tolCmd.sizeMeasured

        # 形位公差评价对象自身的尺寸信息
        for i in range(1, tolCmd.sizeCountCombined + 1):
            data = PcdmisTools.dataTemplate.copy()
            data['命令名'] = id + ' 尺寸'
            data['特征'] = sizeText(i)
            data['轴'] = sizeAxis(i)
            data['单位'] = reportUnits
            data['标称值'] = round(sizeNominal(i), precision)
            data['上公差'] = round(sizePlusTol(i), precision)
            if not PcdmisTools.showNegative:
                sizeMinusTolValue = -sizeMinusTol(i)
            else:
                sizeMinusTolValue = sizeMinusTol(i)
            data['下公差'] = round(sizeMinusTolValue, precision)
            data['上限值'] = round(sizeNominal(i) + sizePlusTol(i), precision)
            data['下限值'] = round(sizeNominal(i) + sizeMinusTolValue, precision)

            data['实测值'] = round(sizeMeasured(i), precision)
            data['类型'] = PcdmisTools.dataType.FCFDIM

            datas.append(data)

        id = tolCmd.ID
        featureID = tolCmd.FeatureID
        segmentAxis = tolCmd.SegmentAxis
        segmentDimNominal = tolCmd.segmentDimNominal
        segmentDimPlusTol = tolCmd.segmentDimPlusTol
        segmentDimMeasured = tolCmd.segmentDimMeasured
        segmentDimBonus = tolCmd.SegmentDimBonus

        # 形位公差
        for i in range(1, tolCmd.SegmentCount + 1):
            for j in range(1, tolCmd.FeatureCount + 1):
                data = PcdmisTools.dataTemplate.copy()
                data['命令名'] = id
                data['特征'] = featureID(j)
                data['轴'] = segmentAxis(j)
                data['单位'] = tolCmd.ReportUnits
                data['标称值'] = round(segmentDimNominal(i, j), precision)
                data['上公差'] = round(segmentDimPlusTol(i, j), precision)
                data['上限值'] = data['上公差']
                data['实测值'] = round(segmentDimMeasured(i, j), precision)
                data['补偿值'] = round(segmentDimBonus(i, j), precision)
                data['类型'] = PcdmisTools.dataType.FCF

                datas.append(data)

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

        # 如果测量程序中赋值了 SN 变量，则优先将这个变量的值作为序列号
        SERIALNUMBER_var = PcdmisTools.part.GetVariableValue('SN').StringValue
        if SERIALNUMBER_var:
            serialNumber = SERIALNUMBER_var
        else:
            serialNumber = PcdmisTools.part.SerialNumber

        return serialNumber, dataList
    
    def modifySerialNumber(sn: str):
        """
        修改序列号

        Args:
            sn(str): 序列号
        """
        PcdmisTools.part.SerialNumber = sn
        PcdmisTools.part.ReportWindow.RefreshReport
    
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
        
