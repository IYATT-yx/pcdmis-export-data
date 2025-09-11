from dialog import Dialog
import constants
from customexception import CustomException
from commontools import CommonTools
from pcdmistools import PcdmisTools
from exceltools import ExcelTools
from mainui import MainUI
from customargparse import CustomArgParse

import argparse
import tkinter
import sys
from typing import Callable
import traceback
from tkinter import filedialog
import os
import datetime
import time
import subprocess
import shutil

def argumentParser() -> argparse.Namespace:
    """
    参数解析

    Returns:
        argparse.Namespace: 参数解析器
    """
    parser = CustomArgParse(description='PC-DMIS 数据导出工具')
    fileGroup = parser.add_mutually_exclusive_group(required=True)
    fileGroup.add_argument('-d', '--directory', type=str, help='指定导出目录')
    fileGroup.add_argument('-dr', '--specifydirectoryatruntime', action='store_true', help='运行时指定导出目录')
    fileGroup.add_argument('-f', '--file', type=str, help='指定导出文件')
    fileGroup.add_argument('-fr', '--specifyfileatruntime', action='store_true', help='运行时指定导出文件')
    fileGroup.add_argument('-n', '--nospecified', action='store_true', help='不指定导出文件或目录')
    return parser.parse_args()

def generateExportFilePath(args: argparse.Namespace, version: str, name: str, serialNumber: str, timeTuple) -> tuple[str, str]:
    """
    根据使用的参数生成导出Excel路径和程序副本路径

    Args:
        args: 参数解析器
        version: PC-DMIS 版本
        name: PC-DMIS 程序名
        timeTuple: 时间元组 time.localtime()

    Returns:
        (str, str): (导出Excel路径, 程序副本路径)
    """
    name = CommonTools.removeFileExtension(name)

    exportProgramFileName = (
        f'{name}'
        f'({version})'
        f'({CommonTools.getTimeStamp(timeTuple, 1)})'
        f'({CommonTools.getTimeStamp(timeTuple, 4)})'
        f'({serialNumber})'
        '.PRG'
    )
    """程序副本文件名"""

    exportExcelFileName = (
        f'{name}'
        f'({version})'
        '.xlsx'
    )
    """默认Excel文件名"""

    defaultExcelFileDir = os.path.join(constants.Path.defaultDataPath, name)
    """默认Excel保存目录"""

    # 指定目录
    if args.directory is not None:
        directory: str = args.directory.strip()
        if directory == '':
            raise CustomException('导出目录为空', CustomException.WARNING)
        exportExcelFilePath = os.path.join(directory, exportExcelFileName)
    # 运行时指定目录
    elif args.specifydirectoryatruntime:
        directory = filedialog.askdirectory(
            initialdir=CommonTools.getInitFolder(),
            title='选择导出目录',
            mustexist=True
        )
        if directory == '':
            Dialog.log('取消选择文件夹', Dialog.INFO)
            return None, None
        CommonTools.setInitFolder(directory)
        exportExcelFilePath = os.path.join(directory, exportExcelFileName)
    # 参数传入文件
    elif args.file is not None:
        file: str = args.file.strip()
        if file == '':
            raise CustomException('导出文件路径为空', CustomException.WARNING)
        dir = os.path.dirname(file)
        exportExcelFilePath = os.path.abspath(file)
    # 运行时选择文件
    elif args.specifyfileatruntime:
        file = filedialog.askopenfilename(
            initialdir=CommonTools.getInitFileDir(),
            title='选择导出文件',
            filetypes=[('Excel 工作簿', '*.xlsx')]
        )
        if file == '':
            Dialog.log('取消选择文件', Dialog.INFO)
            return None, None
        CommonTools.setInitFileDir(file)
        exportExcelFilePath = os.path.abspath(file)
    # 不指定文件或文件夹
    elif args.nospecified:
        exportExcelFilePath = os.path.join(defaultExcelFileDir, exportExcelFileName)
    else:
        raise CustomException('命令行参数错误', CustomException.ERROR)

    # 导出 Excel 的文件夹不存在就自动创建
    dir = os.path.dirname(exportExcelFilePath)
    os.makedirs(dir, exist_ok=True)

    # 整理 Excel 导出路径
    exportExcelFilePath = os.path.normpath(exportExcelFilePath).strip()
    # 程序副本路径
    exportProgramFilePath = os.path.join(dir, exportProgramFileName)

    return exportExcelFilePath, exportProgramFilePath

def newConsolePrint(message: str, delay: int = 3):
    """
    打开新的控制台窗口并打印信息

    Args:
        message (str): 打印的信息
        delay (int, optional): 控制台窗口的存活时间，单位为秒. 默认 3 秒.
    """
    command = f"echo {message} & timeout /t {delay}"
    subprocess.Popen(f'start cmd /c "{command}"', shell=True)

def cmdMode():
    """
    命令模式
    """
    startTime = datetime.datetime.now()
    args = argumentParser()
    pcdmisVersion, programName, fullProgramName = PcdmisTools.connect()

    timeTuple = time.localtime()
    serialNumber, dataList = PcdmisTools.getData()

    exportExcelFilePath, exportProgramFilePath = generateExportFilePath(args, pcdmisVersion, programName, serialNumber, timeTuple)

    if exportExcelFilePath is None:
        Dialog.log('取消选择文件夹或文件')
        return
    
    ExcelTools.openExcel(exportExcelFilePath)
    nonconformingDimensions = ExcelTools.write(serialNumber, dataList, timeTuple)

    print(f'exportProgramFilePath={exportProgramFilePath}')
    if PcdmisTools.saveProg(): # 保存测量程序
        shutil.copy2(PcdmisTools.getCurProgPath(), exportProgramFilePath) # 复制测量程序到指定目录
        CommonTools.setFileReadOnly(exportProgramFilePath) # 设置测量程序只读

    executionTime = datetime.datetime.now() - startTime
    msg = f'程序文件副本：{exportProgramFilePath}，导出 Excel 文件到：{exportProgramFilePath}，耗时：{executionTime}'
    Dialog.log(msg)

    if nonconformingDimensions > 0:
        row = f'{CommonTools.getTimeStamp(timeTuple, 0)},{fullProgramName},{nonconformingDimensions}\n'
        nonconformingDimensionsFile = constants.Path.nonconformingDimensionsFile + CommonTools.getTimeStamp(timeTuple, 1) + '.csv'
        nonconformingDimensionsFolder = os.path.dirname(nonconformingDimensionsFile)
        os.makedirs(nonconformingDimensionsFolder, exist_ok=True)
        if not os.path.exists(nonconformingDimensionsFile):
            with open(nonconformingDimensionsFile, 'w') as f:
                f.write('日期_时间,检测程序路径,不合格尺寸数量\n')
                f.write(row)
        else:
            CommonTools.setFileReadOnly(nonconformingDimensionsFile, False)
            with open(nonconformingDimensionsFile, 'a') as f:
                f.write(row)
        CommonTools.setFileReadOnly(nonconformingDimensionsFile, True)

    # newConsolePrint(msg)

def uiMode():
    """
    图形界面模式
    """
    master = tkinter.Tk()
    master.attributes('-topmost', True)

    master.title(constants.Basic.projectName)

    width = 756
    height = 290
    defaultX = int((master.winfo_screenwidth() - width) / 2)
    defaultY = int((master.winfo_screenheight() - height) / 2)
    master.geometry(f'{width}x{height}+{defaultX}+{defaultY}')
    master.resizable(False, False)

    master.iconbitmap(constants.Basic.logoPath)

    mui = MainUI(master)
    master.mainloop()

def runWithCatchException(func: Callable):
    """
    异常捕捉
    """
    try:
        func()
    except CustomException as ce:
        Dialog.log(traceback.format_exc(), ce.type())
    except Exception:
        Dialog.log(traceback.format_exc(), Dialog.ERROR)

def main():
    Dialog()
    if len(sys.argv) > 1:
        runWithCatchException(cmdMode)
    else:
        runWithCatchException(uiMode)

if __name__ == '__main__':
    status, error =CommonTools.runAsAdmin()
    if status is None:
        main()
    else:
        print(f'{status} {error}')