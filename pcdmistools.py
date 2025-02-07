"""
PC-DMIS 版本:
                    2018 R1
                    2019 R2
                    2023.2
                    
"""
from customexception import CustomException
from dialog import Dialog
import constants

import win32com.client as wc
import hashlib
import re
import importlib
from types import MethodType
from enum import Enum, auto

Dialog()

class PcdmisTools:
    app = None
    part = None
    cmds = None
    pdconst = None
    pivotVersion = '2022'
    getFcfFromCmd: MethodType = None

    @staticmethod
    def importPcdlrnConst(version: str):
        packageName = 'pcdlrnconst'
        moduleName = packageName + '.' + packageName + re.sub(r'[ .]', '', version)
        try:
            PcdmisTools.pdconst = importlib.import_module(moduleName, packageName).constants
        except ModuleNotFoundError:
            raise ValueError(f'未找到 {version} 版本的模块')
        
    @staticmethod
    def initPcdlrnTools(version: str):
        if version >= PcdmisTools.pivotVersion:
            PcdmisTools.importPcdlrnConst('2023.2')
            PcdmisTools.getFcfFromCmd = PcdmisTools.getFcfFromCmd20232
        else:
            PcdmisTools.importPcdlrnConst('2019 R2')
            PcdmisTools.getFcfFromCmd = PcdmisTools.getFcfFromCmd2019R2

    @staticmethod
    def connect() -> tuple[str, str]:
        """
        连接 PC-DMIS

        Returns:
            (PC-DMIS 版本, 当前程序名称)
        """
        if PcdmisTools.app is not None:
            Dialog.log('PC-DMIS 已经连接')
        else:
            PcdmisTools.app = wc.Dispatch('PCDLRN.Application')
            if PcdmisTools.app is None:
                raise CustomException('连接 PC-DMIS 失败', CustomException.CRITICAL)
            else:
                Dialog.log(f'连接 PC-DMIS 成功，版本：{PcdmisTools.app.VersionString}')
        
        PcdmisTools.part = PcdmisTools.app.ActivePartProgram
        PcdmisTools.cmds = PcdmisTools.part.Commands
        if PcdmisTools.part is None:
            raise CustomException('获取当前程序失败', CustomException.CRITICAL)
        else:
            Dialog.log(f'连接 PC-DMIS 程序成功，程序名：{PcdmisTools.part.Name}')
            PcdmisTools.initPcdlrnTools(PcdmisTools.app.VersionString)

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
        measured = cmd.GetFieldValue(PcdmisTools.pdconst.DIM_MEASURED, 0)
        if measured != False: # 排除形位公差和基准
            PcdmisTools.clearData()
            PcdmisTools.data['命令名'] = dim.ID
            PcdmisTools.data['特征'] = dim.Feat1 + ' ' + dim.Feat2 + ' ' + dim.Feat3
            PcdmisTools.data['单位'] = cmd.GetFieldValue(PcdmisTools.pdconst.UNIT_TYPE, 0)
            if cmd.GetFieldValue(PcdmisTools.pdconst.AXIS, 0) == False and PcdmisTools.cmds[idx + 1].ID == '': # 这是一个位置命令，继续下一条命令
                idx += 1
                cmd = PcdmisTools.cmds[idx]
                dim = cmd.DimensionCommand
            PcdmisTools.data['轴'] = dim.AxisLetter
            PcdmisTools.data['标称值'] = round(dim.NOMINAL, precision)
            PcdmisTools.data['上公差'] = round(dim.Plus, precision)
            PcdmisTools.data['下公差'] = round(dim.Minus, precision)
            PcdmisTools.data['上限值'] = round(dim.NOMINAL + dim.Plus, precision)
            PcdmisTools.data['下限值'] = round(dim.NOMINAL + dim.Minus, precision)
            PcdmisTools.data['实测值'] = round(dim.Measured, precision)
            PcdmisTools.data['补偿值'] = round(dim.Bonus, precision)
            PcdmisTools.data['类型'] = PcdmisTools.dataType.DIMENSION
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
        for i in range(1, cmd.GetDataTypeCount(PcdmisTools.pdconst.LINE1_MEAS) + 1):
            PcdmisTools.clearData()
            PcdmisTools.data['单位'] = cmd.GetFieldValue(PcdmisTools.pdconst.UNIT_TYPE, 0)
            PcdmisTools.data['命令名'] = cmd.GetFieldValue(PcdmisTools.pdconst.LINE1_TBLHDR, i)
            PcdmisTools.data['特征'] = cmd.GetFieldValue(PcdmisTools.pdconst.LINE1_FEATNAME, i)
            PcdmisTools.data['轴'] = None

            nominal = cmd.GetFieldValue(PcdmisTools.pdconst.LINE1_NOMINAL, i)
            PcdmisTools.data['标称值'] = round(nominal, precision)

            plus = cmd.GetFieldValue(PcdmisTools.pdconst.LINE1_PLUSTOL, i)
            PcdmisTools.data['上公差'] = round(plus, precision)

            minustol = cmd.GetFieldValue(PcdmisTools.pdconst.LINE1_MINUSTOL, i)
            PcdmisTools.data['下公差'] = round(minustol, precision)

            meas = cmd.GetFieldValue(PcdmisTools.pdconst.LINE1_MEAS, i)
            PcdmisTools.data['实测值'] = round(meas, precision)

            bonus = cmd.GetFieldValue(PcdmisTools.pdconst.LINE1_BONUS, i)
            PcdmisTools.data['补偿值'] = round(bonus, precision)

            PcdmisTools.data['类型'] = PcdmisTools.dataType.FCFDIM

            datas.append(PcdmisTools.data.copy())

        # 形位公差
        for i in range(1, cmd.GetDataTypeCount(PcdmisTools.pdconst.LINE2_MEAS) + 1):
            PcdmisTools.clearData()
            PcdmisTools.data['单位'] = cmd.GetFieldValue(PcdmisTools.pdconst.UNIT_TYPE, 0)

            runoutType = cmd.GetFieldValue(PcdmisTools.pdconst.FCF_RUNOUT_TYPE, i)
            if runoutType == False:
                runoutType = ''
            else:
                runoutType = ' - ' + runoutType

            PcdmisTools.data['命令名'] = cmd.GetFieldValue(PcdmisTools.pdconst.LINE2_TBLHDR, i) + runoutType
            PcdmisTools.data['特征'] = cmd.GetFieldValue(PcdmisTools.pdconst.LINE2_FEATNAME, i)
            PcdmisTools.data['轴'] = cmd.GetFieldValue(PcdmisTools.pdconst.LINE2_AXIS, i)

            nominal = cmd.GetFieldValue(PcdmisTools.pdconst.LINE2_NOMINAL, i)
            PcdmisTools.data['标称值'] = round(nominal, precision)

            plus = cmd.GetFieldValue(PcdmisTools.pdconst.LINE2_PLUSTOL, i)
            PcdmisTools.data['上公差'] = round(plus, precision)

            minustol = cmd.GetFieldValue(PcdmisTools.pdconst.LINE2_MINUSTOL, i)
            PcdmisTools.data['下公差'] = round(minustol, precision)

            PcdmisTools.data['上限值'] = PcdmisTools.data['上公差']

            meas = cmd.GetFieldValue(PcdmisTools.pdconst.LINE2_MEAS, i)
            PcdmisTools.data['实测值'] = round(meas, precision)

            bonus = cmd.GetFieldValue(PcdmisTools.pdconst.LINE2_BONUS, i)
            PcdmisTools.data['补偿值'] = round(bonus, precision)

            PcdmisTools.data['类型'] = PcdmisTools.dataType.FCF

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

        fcfDatas = []

        for i in range(1, tolCmd.sizeCountCombined + 1):
            data = {
                '命令名': tolCmd.ID,
                '特征': tolCmd.sizeText(i),
                '轴': tolCmd.SizeAxis(i),
                '单位': tolCmd.ReportUnits,
                '标称值': round(tolCmd.sizeNominal(i), precision),
                '上公差': round(tolCmd.sizePlusTol(i), precision),
                '下公差': round(tolCmd.sizeMinusTol(i), precision),
                '实测值': round(tolCmd.sizeMeasured(i), precision),
            }
            fcfDatas.append(data.copy())

        for i in range(1, tolCmd.SegmentCount + 1):
            for j in range(1, tolCmd.SegmentCount + 1):
                data = {
                    '命令名': tolCmd.ID,
                    '特征': tolCmd.FeatureID(j),
                    '轴': tolCmd.SegmentAxis(j),
                    '单位': tolCmd.ReportUnits,
                    '标称值': round(tolCmd.segmentDimNominal(i, j), precision),
                    '上公差': round(tolCmd.segmentDimPlusTol(i, j), precision),
                    '下公差': round(tolCmd.segmentDimMinusTol(i, j), precision),
                    '实测值': round(tolCmd.segmentDimMeasured(i, j), precision),
                }
                fcfDatas.append(data.copy())
        return fcfDatas, idx

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

        serialNumber = PcdmisTools.cmds[0].GetFieldValue(PcdmisTools.pdconst.SERIAL_NUMBER, 0)

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
            values = list(data.values())[:-1] # 最后一个键值是测量结果，取测量项目时不需要
            for value in values:
                sumaryString += f'{value}'
        return hashlib.sha256(sumaryString.encode('utf-8')).hexdigest()
    
    @staticmethod
    def addExternalCommand(exePath: str):
        """
        添加外部命令

        Params:
            exePath: 外部命令的路径
        """
        if PcdmisTools.cmds is None:
            raise CustomException('请先连接 PC-DMIS 程序后，再添加命令', CustomException.WARNING)
        cmd = PcdmisTools.cmds.Add(PcdmisTools.pdconst.EXTERNAL_COMMAND, True)

        cmd.PutText(exePath, PcdmisTools.pdconst.COMMAND_STRING, 0)
        cmd.PutText('不显示', PcdmisTools.pdconst.DISPLAY_TRACE, 0)
        cmd.PutText('等待', PcdmisTools.pdconst.TRACE_NAME, 0)
        
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