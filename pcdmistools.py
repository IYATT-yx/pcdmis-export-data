"""
已测试 PC-DMIS 版本:
                    2019 R2
                    
"""
from pcdlrnconst import constants as pdconst
from customexception import CustomException
from dialog import Dialog
from constant import Constant

import win32com.client as wc
import hashlib

Dialog(Constant.Dialog)

class PcdmisTools:
    app = None
    part = None
    cmds = None

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
    def getDimensionFromCmd(cmd, precision) -> list[dict]:
        """
        从测量命令对象中获取尺寸数据

        Params:
            cmd: 测量命令对象
            precision: 浮点数精度

        Returns:
            [ {'命令名': , '特征': , '轴': , '单位': , '标称值': , '上公差': , '下公差': , '实测值': } ]
        """
        if not cmd.isDimension:
            raise CustomException('该命令不是尺寸', CustomException.WARNING)

        dim = cmd.DimensionCommand
        if dim is None:
            Dialog.log('获取尺寸对象失败', Dialog.WARNING)
            return None
        
        id = cmd.ID
        unit = cmd.GetFieldValue(pdconst.UNIT_TYPE, 0)
        # 获取单位失败的话，这个命令可能是一个基准，直接跳过
        if unit == False:
            return None
        
        # 位置的特征名和尺寸数据不在同一条命令中，但在相邻命令
        if len(id) != 0:
            PcdmisTools.data['命令名'] = cmd.ID
            PcdmisTools.data['特征'] = dim.Feat1 + \
                                    (' - ' + dim.Feat2 if dim.Feat2 else '')  + \
                                    (' - ' + dim.Feat3 if dim.Feat3 else '')
            PcdmisTools.data['单位'] = unit
            PcdmisTools.data['单位'] = unit
        # 如果当前命令读取 AxisLetter 失败，那么这个命令就读取不到尺寸数据
        axisLetter = cmd.GetFieldValue(pdconst.AXIS, 0)
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

            return [PcdmisTools.data.copy()]
        
        return None
    
    @staticmethod
    def getFcfFromCmd(cmd, precision) -> list[dict]:
        """
        从测量命令对象中获取形位公差数据

        Params:
            cmd: 测量命令对象
            precision: 浮点数精度

        Returns:
            [ {'命令名': , '特征': , '轴': , '单位': , '标称值': , '上公差': , '下公差': , '实测值': } ]
        """
        if not cmd.isFCFCommand:
            raise CustomException('该命令不是形位公差', CustomException.WARNING)
        
        fcfDatas = []
        data = {
            '命令名': cmd.ID,
            '特征': None,
            '轴': None,
            '单位': cmd.GetFieldValue(pdconst.UNIT_TYPE, 0),
            '标称值': None,
            '上公差': None,
            '下公差': None,
            '实测值': None,
        }

        for i in range(1, cmd.GetDataTypeCount(pdconst.LINE2_MEAS) + 1):
            data['特征'] = cmd.GetFieldValue(pdconst.LINE2_FEATNAME, i)
            data['轴'] = cmd.GetFieldValue(pdconst.LINE2_AXIS, i)

            nominal = cmd.GetFieldValue(pdconst.LINE2_NOMINAL, i)
            if nominal != False:
                nominal = round(nominal, precision)
            data['标称值'] = nominal

            plus = cmd.GetFieldValue(pdconst.LINE2_PLUSTOL, i)
            if plus != False:
                plus = round(plus, precision)
            data['上公差'] = plus

            minustol = cmd.GetFieldValue(pdconst.LINE2_MINUSTOL, i)
            if minustol != False:
                minustol = round(minustol, precision)
            data['下公差'] = minustol

            meas = cmd.GetFieldValue(pdconst.LINE2_MEAS, i)
            if meas != False:
                meas = round(meas, precision)
            data['实测值'] = meas

            fcfDatas.append(data.copy())

        return fcfDatas

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
        for i in range(1, PcdmisTools.cmds.count):
            cmd = PcdmisTools.cmds[i]

            if cmd.IsDimension:
                dimensionData = PcdmisTools.getDimensionFromCmd(cmd, precision)
                if dimensionData is None:
                    continue
                dataList += dimensionData
            elif cmd.IsFCFCommand:
                fcfDatas = PcdmisTools.getFcfFromCmd(cmd, precision)
                dataList += fcfDatas

        serialNumber = PcdmisTools.cmds[0].GetFieldValue(pdconst.SERIAL_NUMBER, 0)

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
        digest = hashlib.sha256(sumaryString.encode('utf-8')).hexdigest()
        Dialog.log(f'测量项目字符串摘要：{digest}')
        return digest
    
    @staticmethod
    def addExternalCommand(exePath: str):
        """
        添加外部命令

        Params:
            exePath: 外部命令的路径
        """
        if PcdmisTools.cmds is None:
            raise CustomException('请先连接 PC-DMIS 程序后，再添加命令', CustomException.WARNING)
        cmd = PcdmisTools.cmds.Add(pdconst.EXTERNAL_COMMAND, True)

        cmd.PutText(exePath, pdconst.COMMAND_STRING, 0)
        cmd.PutText('不显示', pdconst.DISPLAY_TRACE, 0)
        cmd.PutText('等待', pdconst.TRACE_NAME, 0)
        
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