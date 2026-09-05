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
     compiledObj = globals().get('__compiled__')
     isCompiled = compiledObj is not None

class Path:
    appDir = os.path.dirname(__file__)
    enterDir = os.path.dirname(os.path.abspath(sys.argv[0]))
    executableCommandString = os.path.abspath(sys.argv[0]) if Status.isCompiled else sys.executable + ' ' + os.path.abspath(sys.argv[0])
    defaultDataPath = os.path.join(enterDir, 'data')

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
        logoPath = os.path.join(Path.appDir, logoName)
