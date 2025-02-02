"""
常量
"""
from commontools import CommonTools
import os
import logging
import sys

description = """
1 适用：
    1.1 PC-DMIS 版本：2019 R2（其它未测试）
    1.2 Windows 版本：Windows 7 以上，不含 Windows 7
2 使用：
    2.1 请先保证 PC-DMIS 已经启动，且打开了一个测量程序。
    2.2 可以选择指定目录、运行时指定目录、指定文件、运行时指定文件、不指定（导出文件），选择后会生成相应的适用命令。可以复制命令打开终端执行，点击添加命令会在 PC-DMIS 测量程序中光标所在位置添加外部命令，建议先按 Ctrl + END 将光标移动到测量程序尾部，再点击添加命令。
    2.3 凡是没有明确指定导出文件名的，命名采用：[测量程序名][PC-DMIS版本][日期].xlsx，不存在文件则创建，存在则继续追加。
    2.4 如果选择了不指定，那么导出文件的目录就是当前程序所在目录。
"""

class Constant:
    class Basic:
        projectName = 'PC-DMIS 数据导出工具'
        version = '202502020001'
        author = 'IYATT-yx iyatt@iyatt.com'
        description = f'{projectName}\n{version}\n{author}\n\n{description}'
        logoName = 'icon.ico'
        logoPath = os.path.join(sys._MEIPASS, logoName) if CommonTools.getPackagedStatus() else logoName

    class Dialog:
        dialogPath = os.path.join(
            CommonTools.getHomePath(),
            f'PC-DMIS-export-data {CommonTools.getTimeStamp(1)}.log'
        )
        dialogFormat = '[ %(asctime)s %(levelname)-8s 模块：%(name)-16s ] %(message)s'
        dateFormat = '%Y-%m-%d %H:%M:%S'
        dialogLevel = logging.DEBUG
        dialogEncoding = 'utf-8'