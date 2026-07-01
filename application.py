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
import dataprocessor
from topmessagebox import TopMessagebox

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
        self.onUpdate()

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

    def useCmdTabUI(self, tabFrame: tk.Frame):
        """
        “使用命令”标签界面

        Param:
            tabFrame: 父容器
        """
        # 命令输出框
        self.cmdText = tk.Text(tabFrame, width = 105, height=5, state='disabled')
        self.cmdText.grid(column=0, row=0, columnspan=4, rowspan=4, sticky=tk.NSEW)

        # 第一行功能按钮
        tk.Button(tabFrame, text='复制命令', command=self.onCopyButton) \
        .grid(column=0, row=4, sticky=tk.NSEW, padx=5, pady=5)
        tk.Button(tabFrame, text='保存程序', command=lambda: PcdmisTools.connectPcDmis(True)) \
        .grid(column=1, row=4, sticky=tk.NSEW, padx=5, pady=5)
        tk.Button(tabFrame, text='打开数据目录', command=self.onOpenDataDir) \
        .grid(column=2, row=4, sticky=tk.NSEW, padx=5, pady=5)
        tk.Button(tabFrame, text='重置默认配置', command=self.onResetConfig) \
        .grid(column=3, row=4, sticky=tk.NSEW, padx=5, pady=5)

        ttk.Separator(tabFrame, orient='horizontal') \
        .grid(column=0, row=5, columnspan=4, sticky=tk.NSEW)

        # 第二行功能按钮
        tk.Button(tabFrame, text='添加本工具', command=self.onAddCmd) \
        .grid(column=0, row=6, sticky=tk.NSEW, padx=5, pady=5)
        self.isSaveProg = tk.BooleanVar(self, value=True)
        tk.Checkbutton(tabFrame, text='保存测量程序副本', variable=self.isSaveProg, command=self.onUpdate) \
        .grid(column=1, row=6, sticky=tk.W)
        self.isExportPdf = tk.BooleanVar(self, value=False)
        tk.Checkbutton(tabFrame, text='保存PDF报告', variable=self.isExportPdf, command=self.onUpdate) \
        .grid(column=2, row=6, sticky=tk.W)
        tk.Button(tabFrame, text='移除本工具', command=self.onRemoveTool) \
        .grid(column=3, row=6, sticky=tk.NSEW, padx=5, pady=5)

        ttk.Separator(tabFrame, orient='horizontal') \
        .grid(column=0, row=7, columnspan=4, sticky=tk.NSEW)

        # 第三行功能按钮
        tk.Button(tabFrame, text='添加序列号输入', command=self.onAddInputSN) \
        .grid(column=0, row=8, sticky=tk.NSEW, padx=5, pady=5)

        self.isForceEnMode = tk.BooleanVar(self, value=True)
        tk.Checkbutton(tabFrame, text='强制切换英语键盘输入', variable=self.isForceEnMode, command=self.onUpdate) \
        .grid(column=1, row=8, sticky=tk.W)
        tk.Label(tabFrame, text='注：插入位置在活动光标后') \
        .grid(column=2, row=8, sticky=tk.W)

        tk.Button(tabFrame, text='移除序列号输入', command=self.onRemoveInputSN) \
        .grid(column=3, row=8, sticky=tk.NSEW, padx=5, pady=5)

        # 第四行：输出目录
        ttk.Separator(tabFrame, orient='horizontal') \
        .grid(column=0, row=9, columnspan=4, sticky=tk.NSEW)

        tk.Label(tabFrame, text='输出目录（留空使用默认 data 目录）：') \
        .grid(column=0, row=10, columnspan=4, sticky=tk.W, padx=5, pady=(5, 0))
        self.outputPath = tk.StringVar(self)
        outputPathFrame = tk.Frame(tabFrame)
        outputPathFrame.grid(column=0, row=11, columnspan=4, sticky=tk.NSEW, padx=5)
        tk.Entry(outputPathFrame, textvariable=self.outputPath) \
        .pack(side='left', fill='x', expand=True)
        tk.Button(outputPathFrame, text='浏览', command=self.onBrowseOutput) \
        .pack(side='left', padx=(5, 0))
        self.outputPath.trace_add('write', lambda *args: self.onUpdate())

    def onBrowseOutput(self):
        path = filedialog.askdirectory(title='选择输出目录')
        if path:
            self.outputPath.set(path)

    def onOpenDataDir(self):
        dataPath = self.outputPath.get().strip() or constants.Path.defaultDataPath
        if os.path.exists(dataPath):
            os.startfile(dataPath)
        else:
            os.makedirs(dataPath, exist_ok=True)
            os.startfile(dataPath)

    def onResetConfig(self):
        self.isSaveProg.set(True)
        self.isExportPdf.set(False)
        self.isForceEnMode.set(True)
        self.outputPath.set('')
        self.onUpdate()

    def onRemoveInputSN(self):
        self.writeCmdText('正在移除......', False)
        self.update_idletasks()
        pd = PcdmisTools()
        pd.connectPcDmis()
        pd.removeInputCommentAndSN()
        self.master.after(100, self.onUpdate)

    def onAddInputSN(self):
        pd = PcdmisTools()
        pd.connectPcDmis()
        pd.addInputCommentAndSN(self.isForceEnMode.get())
    
    def onRemoveTool(self):
        """
        删除命令按钮事件回调
        """
        self.writeCmdText('正在移除......', False)
        self.update_idletasks()
        PcdmisTools.connectPcDmis()
        PcdmisTools.removeTool()
        self.master.after(100, self.onUpdate)

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
        if addExePath:
            text = constants.Path.executableCommand + ' ' + text
        self.cmdText.insert('1.0', text)
        self.cmdText.config(state='disabled')

    def onCopyButton(self):
        """
        复制按钮事件回调
        """
        textValue = self.cmdText.get('1.0', 'end').strip()
        self.master.clipboard_clear()
        self.master.clipboard_append(textValue)
        self.master.update()
        self.writeCmdText('已复制', False)
        self.master.after(1000, self.onUpdate)

    def onUpdate(self):
        """
        文件选项单选按钮事件回调
        """
        text = ' -n'
        if not self.isSaveProg.get():
            text += ' --no-prog'
        if self.isExportPdf.get():
            text += ' --export-pdf'
        outputPath = self.outputPath.get().strip()
        if outputPath:
            text += f' -o "{outputPath}"'
        self.writeCmdText(text)

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
        fileGroup.add_argument('-n', action='store_true', help='命令模式占位，表示执行命令工具')

        parser.add_argument('-ep', '--export-pdf', action='store_true', help='导出PDF')
        parser.add_argument('-np', '--no-prog', action='store_true', help='不保存测量程序文件')
        parser.add_argument('-o', '--output', type=str, default='', help='指定数据输出目录（默认：程序目录下的 data 文件夹）')

        return parser.parse_args()
    
    @staticmethod
    def cmdMode():
        args = Application.argumentParser()
        dataprocessor.convertPcdCsvToExcel(dataPath=args.output, noProg=args.no_prog, exportPdf=args.export_pdf)

    @staticmethod
    def uiMode():
        master = tk.Tk()
        master.attributes('-topmost', True)

        master.title(constants.Basic.projectName)

        width = 860
        height = 430
        defaultX = int((master.winfo_screenwidth() - width) / 2)
        defaultY = int((master.winfo_screenheight() - height) / 2)
        master.geometry(f'{width}x{height}+{defaultX}+{defaultY}')
        master.resizable(True, True)

        master.iconbitmap(constants.Basic.logoPath)

        MainUI(master)
        master.mainloop()

    @staticmethod
    def run():
        try:
            if len(sys.argv) > 1:
                Application.cmdMode()
            else:
                Application.uiMode()
        except Exception as e:
            errorMsg = traceback.format_exc()
            logging.error(errorMsg)
            TopMessagebox.show(f'{constants.Basic.projectName} - 顶层错误消息', str(e), TopMessagebox.ERROR)

logging.basicConfig(
    filename= os.path.join(constants.Path.programFileDir, 'error.log'),
    level=logging.ERROR,  # 仅记录 ERROR 及以上级别的日志
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    encoding='utf-8'
)