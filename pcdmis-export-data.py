from dialog import Dialog
from constant import Constant
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
    fileGroup
    return parser.parse_args()

def generateExportFilePath(args: argparse.Namespace, version: str, name: str) -> str:
    """
    根据使用的参数生成导出文件路径

    Args:
        args: 参数解析器
        version: PC-DMIS 版本
        name: PC-DMIS 程序名

    Returns:
        str: 导出文件路径
    """
    exportFileName = f'[{CommonTools.removeFileExtension(name)}][{version}][{CommonTools.getTimeStamp(1)}].xlsx'

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
            initialdir=CommonTools.getMyPath(),
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
        exportFilePath = CommonTools.getAbsPath(file)
    # 运行时选择文件
    elif args.specifyfileatruntime:
        file = filedialog.asksaveasfilename(
            initialdir=CommonTools.getMyPath(),
            title='选择导出文件',
            filetypes=[('Excel 工作簿', '*.xlsx')],
            confirmoverwrite=False,
        )
        if file == '':
            Dialog.log('取消选择文件', Dialog.INFO)
            return
        exportFilePath = CommonTools.getAbsPath(file)
    # 不指定文件或文件夹
    elif args.nospecified:
        exportFilePath = os.path.join(CommonTools.getMyPath(), exportFileName)
    else:
        raise CustomException('命令行参数错误', CustomException.ERROR)

    return os.path.normpath(exportFilePath).strip()

def cmdMode():
    """
    命令模式
    """
    args = argumentParser()
    pcdmisVersion, programName = PcdmisTools.connect()
    exportFilePath = generateExportFilePath(args, pcdmisVersion, programName)
    
    serialNumber, dataList = PcdmisTools.getData()
    ExcelTools.openExcel(exportFilePath)
    ExcelTools.write(serialNumber, dataList)

def uiMode():
    """
    图形界面模式
    """
    master = tkinter.Tk()
    master.attributes('-topmost', True)

    master.title(Constant.Basic.projectName)

    width = 756
    height = 240
    defaultX = int((master.winfo_screenwidth() - width) / 2)
    defaultY = int((master.winfo_screenheight() - height) / 2)
    master.geometry(f'{width}x{height}+{defaultX}+{defaultY}')
    master.resizable(False, False)

    master.iconbitmap(Constant.Basic.logoPath)

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
    Dialog(Constant.Dialog)
    if len(sys.argv) > 1:
        runWithCatchException(cmdMode)
    else:
        runWithCatchException(uiMode)
    Dialog.log('程序结束', Dialog.DEBUG)

if __name__ == '__main__':
    status, error =CommonTools.runAsAdmin()
    if status is None:
        main()
    else:
        print(f'{status} {error}')