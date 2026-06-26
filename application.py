"""
file: application.py
description: 应用程序入口
author: IYATT-yx
copyright:  Copyright (c) 2025-2026 IYATT-yx.
            Licensed under the MIT License. See LICENSE file in the project root for full license information.
"""
from pcdmistools import PcdmisTools
from customargparse import CustomArgParse
import constants
from common import Common
import dataprocessor

import argparse
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
import sys
import logging
import traceback

class MainUI(tk.Frame):
    def __init__(self, master: tk.Tk=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.tabsUI()
        self.afterCreateUserInterface()

    def tabsUI(self):
        """
        标签页布局
        """
        notebook = ttk.Notebook(self.master)
        notebook.pack(fill='both', expand=True)

        useCmdTabFrame = tk.Frame(notebook)
        notebook.add(useCmdTabFrame, text='使用命令')
        self.useCmdTabUI(useCmdTabFrame)

        aboutTabFrame = tk.Frame(notebook)
        notebook.add(aboutTabFrame, text='关于')
        self.aboutTabUI(aboutTabFrame)

    class FileOptions:
        DIRECTORY = 0
        SPECIFYDIRECTORYATRUNTIME = 1
        FILE = 2
        SPECIFYFILEATRUNTIME = 3
        NOSPECIFIED = 4
        
    def useCmdTabUI(self, tabFrame: tk.Frame):
        """
        “使用命令”标签界面

        Param:
            tabFrame: 父容器
        """
        # 文件选项单选按钮
        self.fileOption = tk.IntVar()
        tk.Radiobutton(tabFrame, text='指定目录', variable=self.fileOption, value=MainUI.FileOptions.DIRECTORY, command=self.onFileOptionRadiobutton, state=tk.DISABLED) \
        .grid(column=0, row=0, sticky=tk.W)
        tk.Radiobutton(tabFrame, text='运行时指定目录', variable=self.fileOption, value=MainUI.FileOptions.SPECIFYDIRECTORYATRUNTIME, command=self.onFileOptionRadiobutton, state=tk.DISABLED) \
        .grid(column=0, row=1, sticky=tk.W)
        tk.Radiobutton(tabFrame, text='指定文件', variable=self.fileOption, value=MainUI.FileOptions.FILE, command=self.onFileOptionRadiobutton, state=tk.DISABLED) \
        .grid(column=0, row=2, sticky=tk.W)
        tk.Radiobutton(tabFrame, text='运行时指定文件', variable=self.fileOption, value=MainUI.FileOptions.SPECIFYFILEATRUNTIME, command=self.onFileOptionRadiobutton, state=tk.DISABLED) \
        .grid(column=0, row=3, sticky=tk.W)
        tk.Radiobutton(tabFrame, text='不指定', variable=self.fileOption, value=MainUI.FileOptions.NOSPECIFIED, command=self.onFileOptionRadiobutton) \
        .grid(column=0, row=4, sticky=tk.W)

        # 是否保存程序文件选项
        self.isSaveProg = tk.BooleanVar(self, value=True)
        tk.Checkbutton(tabFrame, text='保存测量程序副本', variable=self.isSaveProg, command=self.onFileOptionRadiobutton) \
        .grid(column=0, row=6, sticky=tk.W)
        # 是否保存 PDF 报告
        self.isExportPdf = tk.BooleanVar(self, value=False)
        tk.Checkbutton(tabFrame, text='保存PDF报告', variable=self.isExportPdf, command=self.onFileOptionRadiobutton) \
        .grid(column=1, row=6, sticky=tk.W)

        # 目录和文件输入框
        self.directoryEntryValue = tk.StringVar()
        self.fileEntryValue = tk.StringVar()
        tk.Entry(tabFrame, textvariable=self.directoryEntryValue, width=80, state=tk.DISABLED) \
        .grid(column=1, row=0, sticky=tk.NSEW)
        self.fileEntry = tk.Entry(tabFrame, textvariable=self.fileEntryValue, width=80, state=tk.DISABLED) \
        .grid(column=1, row=2, sticky=tk.NSEW)

        # 操作按钮
        tk.Button(tabFrame, text='浏览文件夹', command=self.onBrowseFolderButton, state=tk.DISABLED) \
        .grid(column=2, row=0, sticky=tk.NSEW)
        tk.Button(tabFrame, text='浏览文件', command=self.onBrowseFileButton, state=tk.DISABLED) \
        .grid(column=2, row=2, sticky=tk.NSEW)
        tk.Button(tabFrame, text='复制命令', command=self.onCopyButton) \
        .grid(column=0, row=8, sticky=tk.NSEW)
        tk.Button(tabFrame, text='移除工具', command=self.onDelCmd) \
        .grid(column=0, row=9, sticky=tk.NSEW)
        tk.Button(tabFrame, text='添加工具', command=self.onAddCmd) \
        .grid(column=0, row=10, sticky=tk.NSEW)
        tk.Button(tabFrame, text='保存程序', command=lambda: PcdmisTools.connectPcDmis(True)) \
        .grid(column=0, row=11, sticky=tk.NSEW)

        # 分隔线
        ttk.Separator(tabFrame, orient='horizontal').grid(column=0, row=5, columnspan=3, sticky=tk.EW, padx=10, pady=10)
        ttk.Separator(tabFrame, orient='horizontal').grid(column=0, row=7, columnspan=3, sticky=tk.EW, padx=10, pady=10)

        # 命令输出框
        self.cmdText = tk.Text(tabFrame, height=5, state='disabled')
        self.cmdText.grid(column=1, row=8, columnspan=2, rowspan=4, sticky=tk.NSEW)
    
    def onDelCmd(self):
        """
        删除命令按钮事件回调
        """
        PcdmisTools.connectPcDmis()
        PcdmisTools.removeCommand()
        

    def afterCreateUserInterface(self):
        """
        创建用户界面的后续处理工作
        """
        # 设置文件选项单选框默认选中项
        self.fileOption.set(MainUI.FileOptions.NOSPECIFIED)
        self.onFileOptionRadiobutton()

        # 追踪文件夹和文件输入框写操作事件
        self.directoryEntryValue.trace_add('write', self.onFolderEntryChange)
        self.fileEntryValue.trace_add('write', self.onFileEntryChange)

    def onBrowseFolderButton(self):
        """
        浏览文件夹按钮事件回调
        """
        directory = filedialog.askdirectory(
            initialdir=Common.getInitFolder(),
            title='选择导出目录',
            mustexist=True
        )
        if directory == '':
            return
        directory = os.path.normpath(directory)
        Common.setInitFolder(directory)
        self.directoryEntryValue.set(directory)

    def onBrowseFileButton(self):
        """
        浏览文件按钮事件回调
        """
        file = filedialog.askopenfilename(
            initialdir=Common.getInitFileDir(),
            title='选择导出文件',
            filetypes=[('Excel 工作簿', '*.xlsx')]
        )
        if file == '':
            return
        file = os.path.normpath(file)
        Common.setInitFileDir(file)
        self.fileEntryValue.set(file)

    def onFolderEntryChange(self, *args):
        """
        文件夹输入框写操作事件回调

        Params:
            *args: 事件参数 (忽略)
        """
        if self.fileOption.get() != MainUI.FileOptions.DIRECTORY:
            self.fileOption.set(MainUI.FileOptions.DIRECTORY)
        self.writeCmdText(
            '-d "' + self.directoryEntryValue.get().strip() + '"'
        )

    def onFileEntryChange(self, *args):
        """
        文件输入框写操作事件回调

        Params:
            *args: 事件参数 (忽略)
        """
        if self.fileOption.get() != MainUI.FileOptions.FILE:
            self.fileOption.set(MainUI.FileOptions.FILE)
        self.writeCmdText(
            '-f "' + self.fileEntryValue.get().strip() + '"'
        )

    def onCopyButton(self):
        """
        复制按钮事件回调
        """
        textValue = self.cmdText.get('1.0', 'end').strip()
        self.master.clipboard_clear()
        self.master.clipboard_append(textValue)
        self.master.update()
        self.writeCmdText('已复制', False)
        self.master.after(500, self.rewrite, textValue)

    def rewrite(self, text: str):
        self.writeCmdText(text, False)

    def writeCmdText(self, text: str, addExePath: bool = True):
        """
        写命令输出框

        Params:
            text: 要写入的文本
            addExePath: 是否添加可执行文件路径
        """
        self.cmdText.config(state='normal')
        self.cmdText.delete('1.0', 'end')
        if not self.isSaveProg.get():
            text += ' --no-prog'
        if self.isExportPdf.get():
            text += ' --export-pdf'
        if addExePath:
            text = constants.Path.executableCommand + ' ' + text
        self.cmdText.insert('1.0', text)
        self.cmdText.config(state='disabled')

    def onFileOptionRadiobutton(self):
        """
        文件选项单选按钮事件回调
        """
        match self.fileOption.get():
            case MainUI.FileOptions.DIRECTORY:
                self.onFolderEntryChange()
            case MainUI.FileOptions.SPECIFYDIRECTORYATRUNTIME:
                self.writeCmdText('-dr')
            case MainUI.FileOptions.FILE:
                self.onFileEntryChange()
            case MainUI.FileOptions.SPECIFYFILEATRUNTIME:
                self.writeCmdText('-fr')
            case MainUI.FileOptions.NOSPECIFIED:
                self.writeCmdText('-n')
            case _:
                raise RuntimeError('未知选项')

    def onAddCmd(self):
        """
        向 PC-DMIS 中添加外部命令
        """
        PcdmisTools.connectPcDmis()
        if self.isExportPdf.get():
            PcdmisTools.addPdfPathVar()
        commandString = self.cmdText.get('1.0', 'end').strip()
        PcdmisTools.addBasicAndExternalCommand(commandString)
        if self.isExportPdf.get():
            PcdmisTools.addPrintReport()

    def aboutTabUI(self, tabFrame: ttk.Frame):
        """
        “关于”标签界面
        """
        text = tk.Text(tabFrame)
        text.pack(fill='both')
        text.insert('end', constants.Basic.description)
        text.config(state='disabled')

class Application:
    @staticmethod
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

        parser.add_argument('-ep', '--export-pdf', action='store_true', help='导出PDF')
        parser.add_argument('-np', '--no-prog', action='store_true', help='不保存测量程序文件')

        return parser.parse_args()
    
    @staticmethod
    def cmdMode():
        args = Application.argumentParser()
        dataprocessor.convertPcdCsvToExcel(noProg=args.no_prog, exportPdf=args.export_pdf)

    @staticmethod
    def uiMode():
        master = tk.Tk()
        master.attributes('-topmost', True)

        master.title(constants.Basic.projectName)

        width = 756
        height = 370
        defaultX = int((master.winfo_screenwidth() - width) / 2)
        defaultY = int((master.winfo_screenheight() - height) / 2)
        master.geometry(f'{width}x{height}+{defaultX}+{defaultY}')
        master.resizable(False, False)

        master.iconbitmap(constants.Basic.logoPath)

        MainUI(master)
        master.mainloop()

    @staticmethod
    def run():
        try:
            status, error = Common.runAsAdmin()
            if status is None:
                if len(sys.argv) > 1:
                    Application.cmdMode()
                else:
                    Application.uiMode()
            elif status:
                return
            else:
                raise RuntimeError(f'以管理员身份运行失败，错误消息：{error}')
        except Exception as e:
            errorMsg = traceback.format_exc()
            logging.error(errorMsg)
            messagebox.showerror(f'{constants.Basic.projectName} - 顶层错误消息', str(e))

logging.basicConfig(
    filename= os.path.join(constants.Path.programFileDir, 'error.log'),
    level=logging.ERROR,  # 仅记录 ERROR 及以上级别的日志
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    encoding='utf-8'
)