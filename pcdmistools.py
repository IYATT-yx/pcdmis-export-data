"""
PC-DMIS 版本:
                    2019 R2
                    2023.2
                    
"""
from customexception import CustomException
from dialog import Dialog
from constant import Constant

import win32com.client as wc
import hashlib
import re
import importlib
from types import MethodType

Dialog(Constant.Dialog)

class PcdmisTools:
    app = None
    part = None
    cmds = None
    pdconst = None
    pivotVersion = '2022'
    getDimensionFromCmd: MethodType = None
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
            PcdmisTools.getDimensionFromCmd = PcdmisTools.getDimensionFromCmd20232
            PcdmisTools.getFcfFromCmd = PcdmisTools.getFcfFromCmd20232
        else:
            PcdmisTools.importPcdlrnConst('2019 R2')
            PcdmisTools.getDimensionFromCmd = PcdmisTools.getDimensionFromCmd2019R2
            PcdmisTools.getFcfFromCmd = PcdmisTools.getDimensionFromCmd2019R2

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
        
        if PcdmisTools.part is not None:
            Dialog.log(f'已经连接 PC-DMIS 程序')
        else:
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
        '实测值': None,
    }

    dataKeys = list(data.keys())
    dataLen = len(dataKeys)

    @staticmethod
    def getDimensionFromCmd2019R2(idx, cmd, precision) -> list[dict]:
        """
        从测量命令对象中获取尺寸数据

        Params:
            cmd: 测量命令对象
            precision: 浮点数精度

        Returns:
            [ {'命令名': , '特征': , '轴': , '单位': , '标称值': , '上公差': , '下公差': , '实测值': } ]
        """
        if not cmd.isDimension:
            return None, idx

        dim = cmd.DimensionCommand
        if dim is None:
            Dialog.log('获取尺寸对象失败', Dialog.WARNING)
            return None, idx
        
        id = cmd.ID
        unit = cmd.GetFieldValue(PcdmisTools.pdconst.UNIT_TYPE, 0)
        # 获取单位失败的话，这个命令可能是一个基准，直接跳过
        if unit == False:
            return None, idx
        
        # 位置的特征名和尺寸数据不在同一条命令中，但在相邻命令
        if len(id) != 0:
            PcdmisTools.data['命令名'] = cmd.ID
            PcdmisTools.data['特征'] = dim.Feat1 + \
                                    (' - ' + dim.Feat2 if dim.Feat2 else '')  + \
                                    (' - ' + dim.Feat3 if dim.Feat3 else '')
            PcdmisTools.data['单位'] = unit
            PcdmisTools.data['单位'] = unit
        # 如果当前命令读取 AxisLetter 失败，那么这个命令就读取不到尺寸数据
        axisLetter = cmd.GetFieldValue(PcdmisTools.pdconst.AXIS, 0)
        if axisLetter != False:
            PcdmisTools.data['轴'] = axisLetter

            nominal = dim.NOMINAL
            if nominal != False:
                nominal = round(nominal, precision)
            PcdmisTools.data['标称值'] = nominal

            plus = dim.Plus
            if plus != False:
                plus = round(plus, precision)
            PcdmisTools.data['上公差'] = plus

            minus = dim.Minus
            if minus != False:
                minus = round(minus, precision)
            PcdmisTools.data['下公差'] = minus

            measured = dim.Measured
            if measured != False:
                measured = round(measured, precision)
            PcdmisTools.data['实测值'] = measured

            return [PcdmisTools.data.copy()], idx
        
        return None, idx

    @staticmethod
    def getDimensionFromCmd20232(idx, cmd, precision) -> list[dict]:
        """
        从测量命令对象中获取尺寸数据

        Params:
            cmd: 测量命令对象
            precision: 浮点数精度

        Returns:
            [ {'命令名': , '特征': , '轴': , '单位': , '标称值': , '上公差': , '下公差': , '实测值': } ]
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
            PcdmisTools.data['实测值'] = round(dim.Measured, precision)
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
            [ {'命令名': , '特征': , '轴': , '单位': , '标称值': , '上公差': , '下公差': , '实测值': } ]
        """
        if not cmd.isFCFCommand:
            return None, idx
        
        fcfDatas = []
        data = {
            '命令名': cmd.ID,
            '特征': None,
            '轴': None,
            '单位': cmd.GetFieldValue(PcdmisTools.pdconst.UNIT_TYPE, 0),
            '标称值': None,
            '上公差': None,
            '下公差': None,
            '实测值': None,
        }

        for i in range(1, cmd.GetDataTypeCount(PcdmisTools.pdconst.LINE2_MEAS) + 1):
            data['特征'] = cmd.GetFieldValue(PcdmisTools.pdconst.LINE2_FEATNAME, i)
            data['轴'] = cmd.GetFieldValue(PcdmisTools.pdconst.LINE2_AXIS, i)

            nominal = cmd.GetFieldValue(PcdmisTools.pdconst.LINE2_NOMINAL, i)
            if nominal != False:
                nominal = round(nominal, precision)
            data['标称值'] = nominal

            plus = cmd.GetFieldValue(PcdmisTools.pdconst.LINE2_PLUSTOL, i)
            if plus != False:
                plus = round(plus, precision)
            data['上公差'] = plus

            minustol = cmd.GetFieldValue(PcdmisTools.pdconst.LINE2_MINUSTOL, i)
            if minustol != False:
                minustol = round(minustol, precision)
            data['下公差'] = minustol

            meas = cmd.GetFieldValue(PcdmisTools.pdconst.LINE2_MEAS, i)
            if meas != False:
                meas = round(meas, precision)
            data['实测值'] = meas

            fcfDatas.append(data.copy())

        return fcfDatas, idx

    @staticmethod
    def getFcfFromCmd20232(idx, cmd, precision) -> list[dict]:
        """
        从测量命令对象中获取形位公差数据

        Params:
            cmd: 测量命令对象
            precision: 浮点数精度

        Returns:
            [ {'命令名': , '特征': , '轴': , '单位': , '标称值': , '上公差': , '下公差': , '实测值': } ]
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
    def getData(precision: int = 4) -> tuple[str, list[dict]]:
        """
        获取尺寸和形位公差数据

        Params:
            precision: 浮点数精度

        Returns:
            (序列号, [{'命令名': , '特征': , '轴': , '单位': , '标称值': , '上公差': , '下公差': , '实测值': }])
        """
        if PcdmisTools.cmds is None:
            raise CustomException('请先连接 PC-DMIS 程序后，再获取数据', CustomException.WARNING)
        
        dataList = []
        idx = 0
        while idx < PcdmisTools.cmds.Count:
            cmd = PcdmisTools.cmds[idx]
            dimensionData, idx = PcdmisTools.getDimensionFromCmd(idx, cmd, precision)
            if dimensionData is not None:
                dataList += dimensionData
            fcfDatas, idx = PcdmisTools.getFcfFromCmd(idx, cmd, precision)
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