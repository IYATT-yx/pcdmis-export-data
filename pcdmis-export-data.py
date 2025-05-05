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

def generateExportFilePath(args: argparse.Namespace, version: str, name: str, timeTuple) -> str:
    """
    根据使用的参数生成导出文件路径

    Args:
        args: 参数解析器
        version: PC-DMIS 版本
        name: PC-DMIS 程序名
        timeTuple: 时间元组 time.localtime()

    Returns:
        str: 导出文件路径
    """
    pcdmisProgramName = CommonTools.removeFileExtension(name)
    exportFileName = f'{pcdmisProgramName}({version})({CommonTools.getTimeStamp(timeTuple, 1)}).xlsx'
    defaultDir = os.path.join(constants.Path.defaultDataPath, pcdmisProgramName)
    if CommonTools.checkFileExist(defaultDir) == False:
        os.makedirs(defaultDir)
        Dialog.log(f'创建文件夹：{defaultDir}')

    # 指定目录
    if args.directory is not None:
        directory: str = args.directory.strip()
        if directory == '':
            raise CustomException('导出目录为空', CustomException.WARNING)
        if CommonTools.checkFileExist(directory) == False:
            raise CustomException('指定的目录不存在', CustomException.WARNING)
        exportFilePath = os.path.join(directory, exportFileName)
    # 运行时指定目录
    elif args.specifydirectoryatruntime:
        directory = filedialog.askdirectory(
            initialdir=constants.Path.programFileDir,
            title='选择导出目录',
            mustexist=True
        )
        if directory == '':
            Dialog.log('取消选择文件夹', Dialog.INFO)
            return
        exportFilePath = os.path.join(directory, exportFileName)
    # 参数传入文件
    elif args.file is not None:
        file: str = args.file.strip()
        if file == '':
            raise CustomException('导出文件路径为空', CustomException.WARNING)            
        exportFilePath = os.path.abspath(file)
    # 运行时选择文件
    elif args.specifyfileatruntime:
        file = filedialog.asksaveasfilename(
            initialdir=constants.Path.programFileDir,
            title='选择导出文件',
            filetypes=[('Excel 工作簿', '*.xlsx')],
            confirmoverwrite=False,
        )
        if file == '':
            Dialog.log('取消选择文件', Dialog.INFO)
            return
        exportFilePath = os.path.abspath(file)
    # 不指定文件或文件夹
    elif args.nospecified:
        exportFilePath = os.path.join(defaultDir, exportFileName)
    else:
        raise CustomException('命令行参数错误', CustomException.ERROR)

    return os.path.normpath(exportFilePath).strip()

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
    pcdmisVersion, programName = PcdmisTools.connect()

    timeTuple = time.localtime()

    exportFilePath = generateExportFilePath(args, pcdmisVersion, programName, timeTuple)
    
    serialNumber, dataList = PcdmisTools.getData()
    ExcelTools.openExcel(exportFilePath)
    ExcelTools.write(serialNumber, dataList, timeTuple)

    # 保存程序文件路径
    saveAsProgramPath = os.path.join(
        os.path.dirname(exportFilePath),
        CommonTools.removeFileExtension(exportFilePath) + f'({CommonTools.getTimeStamp(timeTuple, 0)})END.PRG'
    )
    if PcdmisTools.saveProg(): # 保存测量程序
        shutil.copy2(PcdmisTools.getCurProgPath(), saveAsProgramPath) # 复制测量程序到指定目录
        CommonTools.setFileReadOnly(saveAsProgramPath) # 设置测量程序只读

    executionTime = datetime.datetime.now() - startTime
    msg = f'导出文件到：{exportFilePath}，耗时：{executionTime}'
    Dialog.log(msg)
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