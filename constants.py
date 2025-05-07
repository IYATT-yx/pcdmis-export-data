"""
常量
"""
import buildtime
from colors import Colors

import os
import logging
import sys
import datetime

class Status:
     packaged = not sys.argv[0].endswith('.py')
     """软件是否处于打包状态"""

class Path:
    runtimeDir = os.path.dirname(__file__)
    """运行时目录"""
    programFileDir = os.path.dirname(os.path.abspath(sys.argv[0]))
    """程序文件所在目录"""
    executableCommand = os.path.abspath(sys.argv[0]) if Status.packaged else sys.executable + ' ' + os.path.abspath(sys.argv[0])
    """软件自身的执行命令"""
    executableFilePath = os.path.abspath(sys.argv[0]) if Status.packaged else sys.executable
    """可执行文件路径"""
    defaultDataPath = os.path.join(programFileDir, 'data')
    """默认数据文件路径"""

description = """
1 适用：
    1.1 PC-DMIS 版本：2018 R1、2019 R2、2023.1、2023.2
    1.2 Windows 版本：Windows 7 以上，不含 Windows 7
2 使用：
    2.1 请先保证 PC-DMIS 已经启动，且打开了一个测量程序。
    2.2 可以选择指定目录、运行时指定目录、指定文件、运行时指定文件、不指定（导出文件），选择后会生成相应的适用命令。可以复制命令打开终端执行，点击添加命令会在 PC-DMIS 测量程序末尾位置添加外部命令。
    2.3 凡是没有明确指定导出文件名的，命名采用：测量程序名(PC-DMIS版本).xlsx，不存在文件则创建，存在则继续追加。另外会尝试自动保存测量程序副本，保存到Excel同目录下。
    2.4 如果选择了不指定，那么会保存到程序目录下的 data 文件夹中。
    2.5 请在设置里勾选“负公差显示负号”，可保证形位公差评价对象的尺寸公差下限和超差判定是正确的。
"""

class Basic:
        projectName = 'PC-DMIS 数据导出工具'
        buildTimeFile = 'buildTime.txt'
        version = buildtime.buildTime
        author = 'IYATT-yx iyatt@iyatt.com'
        description = f'{projectName}\n版本：{version}\n作者：{author}\n\n{description}'
        logoName = 'icon.ico'
        logoPath = os.path.join(Path.runtimeDir, logoName)

class Dialog:
    dialogPath = os.path.join(
        Path.programFileDir,
        'log',
        f'PC-DMIS-export-data_{datetime.datetime.now().strftime('%Y%m%d')}.log'
    )
    dialogFormat = '[ %(asctime)s %(levelname)-8s 模块：%(name)-16s ] %(message)s'
    dateFormat = '%Y-%m-%d %H:%M:%S'
    dialogLevel = logging.DEBUG
    dialogEncoding = 'utf-8'

class Data:
    # 导出数据的精度
    precision = 4
    # 超上差颜色
    overPlusColor = Colors.RED
    # 超下差颜色
    underMinusColor = Colors.MAGENTA





