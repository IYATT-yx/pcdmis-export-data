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

    myDataPath = os.path.join(os.getenv('APPDATA'), 'pcdmis-export-data')
    """用户数据路径"""
    initFolderPath = os.path.join(myDataPath, 'initFolder.txt') # ？？？？
    """用于存储初始文件夹路径的文件路径"""
    initFileDir = os.path.join(myDataPath, 'initFileDir.txt') # ？？？？
    """用于存储初始文件路径的文件路径"""
    nonconformingDimensionsFile = os.path.join(defaultDataPath, '不合格尺寸汇总', '不合格尺寸汇总表')
    """不合格计数文件路径"""
    
description = """
适用：
    PC-DMIS 版本：2018 R1、2019 R2、2023.1、2023.2
    系统版本： Windows 8 及以上
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
    # 合格颜色
    ok = Colors.GREEN
    # 不合格颜色
    ng = Colors.YELLOW





