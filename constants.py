"""
file: constants.py
description: 常量
author: IYATT-yx
copyright:  Copyright (c) 2025-2026 IYATT-yx.
            Licensed under the MIT License. See LICENSE file in the project root for full license information.
"""
import buildtime

import os
import sys

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

    # myDataPath = os.path.join(os.getenv('APPDATA'), 'pcdmis-export-data')
    # """用户数据路径"""
    # initFolderPath = os.path.join(myDataPath, 'initFolder.txt')
    # """用于存储初始文件夹路径的文件路径"""
    # initFileDir = os.path.join(myDataPath, 'initFileDir.txt')
    # """用于存储初始文件路径的文件路径"""
    # nonconformingDimensionsFile = os.path.join(defaultDataPath, '检测记录汇总', '检测记录汇总表')
    # """不合格计数文件路径"""
    
description = """
说明：
    1.本工具为重构版本（第二代），通过 BASIC 脚本提取检测数据，大幅优化性能。
    2.本工具仅支持 Windows 10 及以上的系统。
    3.我会在生产环境持续测试的 PC-DMIS 版本：2018 R1、2020 R1、2023.1。
"""

class Basic:
        projectName = 'PC-DMIS 数据导出工具（第二代）'
        version = buildtime.buildTime
        author = 'IYATT-yx iyatt@iyatt.com'
        repository = 'https://github.com/IYATT-yx/pcdmis-export-data'
        description = f'{projectName}\n版本：{version}\n作者：{author}\n项目开源地址：{repository}\n\n{description}'
        logoName = 'icon.ico'
        logoPath = os.path.join(Path.runtimeDir, logoName)
