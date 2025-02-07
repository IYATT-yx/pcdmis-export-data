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
    executableCommand = os.path.abspath(sys.argv[0]) if Status.packaged else sys.executable + ' ' + os.path.abspath(sys.argv[0])
    """软件的执行命令"""

    rootDir = os.path.dirname(
          sys.executable if Status.packaged else os.path.abspath(sys.argv[0])
    )
    """根目录"""

    programFileDir = os.path.dirname(os.path.abspath(sys.argv[0]))
    """程序文件所在目录"""

    executableFilePath = os.path.abspath(sys.argv[0]) if Status.packaged else sys.executable
    """可执行文件路径"""

    # executableFilePath = os.path.abspath(sys.argv[0])
    # """nuitka 打包后为可执行文件路径；未打包为脚本入口文件路径"""
    # rootPath = os.path.dirname(
    #     sys.executable if CommonTools.getPackagedStatus() else os.path.abspath(sys.argv[0])
    # )
    # """nuitka 打包后为可执行文件释放的临时目录；未打包为脚本入口文件所在目录"""
    # executableFileDir = os.path.dirname(executableFilePath)
    # """nuitka 打包后为可执行文件所在目录，未打包为脚本入口文件所在目录"""

description = """
1 适用：
    1.1 PC-DMIS 版本：2018 R1、2019 R2、2023.1、2023.2
    1.2 Windows 版本：Windows 7 以上，不含 Windows 7
2 使用：
    2.1 请先保证 PC-DMIS 已经启动，且打开了一个测量程序。
    2.2 可以选择指定目录、运行时指定目录、指定文件、运行时指定文件、不指定（导出文件），选择后会生成相应的适用命令。可以复制命令打开终端执行，点击添加命令会在 PC-DMIS 测量程序中光标所在位置添加外部命令，建议先按 Ctrl + END 将光标移动到测量程序尾部，再点击添加命令。
    2.3 凡是没有明确指定导出文件名的，命名采用：[测量程序名][PC-DMIS版本][日期].xlsx，不存在文件则创建，存在则继续追加。
    2.4 如果选择了不指定，那么导出文件的目录就是当前程序所在目录。
    2.5 PC-DMIS 2022 及以上，请在设置里勾选“负公差显示负号”，可保证形位公差评价对象的尺寸公差下限和超差判定是正确的。
"""

class Basic:
        projectName = 'PC-DMIS 数据导出工具'
        buildTimeFile = 'buildTime.txt'
        version = buildtime.buildTime
        author = 'IYATT-yx iyatt@iyatt.com'
        description = f'{projectName}\n版本：{version}\n作者：{author}\n\n{description}'
        logoName = 'icon.ico'
        logoPath = os.path.join(Path.rootDir, logoName)

class Dialog:
    dialogPath = os.path.join(
        Path.programFileDir,
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





