"""
file: application.py
description: 应用程序入口
author: IYATT-yx
copyright:  Copyright (c) 2025-2026 IYATT-yx.
            Licensed under the MIT License. See LICENSE file in the project root for full license information.
"""
import argparse
import tkinter as tk
from tkinter import ttk, filedialog
import os
import sys
import logging
import traceback
import subprocess

from pcdmistools import PcdmisTools
from customargparse import CustomArgParse
import constants
import dataprocessor
from topmessagebox import TopMessagebox
import pdftimeprocessor

class MainUI(tk.Frame):
    class FileOptions:
        '''导出方式'''
        NOSPECIFIED = 0
        DIRECTORY = 1
        FILE = 2

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
        notebook.add(useCmdTabFrame, text='工具')
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
        self.cmdText = tk.Text(tabFrame, height=5, state='disabled')
        self.cmdText.grid(column=0, row=0, columnspan=4, rowspan=4, sticky=tk.NSEW)

        # 列宽等比例自适应
        for i in range(4):
            tabFrame.grid_columnconfigure(i, weight=1)

        # 基础组框
        row = 4
        baseBox = tk.LabelFrame(tabFrame, text='基础', padx=10, pady=10)
        baseBox.grid(column=0, row=row, columnspan=4, sticky=tk.NSEW)
        for i in range(4):
            baseBox.grid_columnconfigure(i, weight=1)
        # 组框内部组件：
        tk.Button(baseBox, text='复制命令', command=self.onCopyButton) \
        .grid(column=0, row=0, sticky=tk.NSEW, padx=5, pady=5)
        tk.Button(baseBox, text='保存程序', command=lambda: PcdmisTools.connectPcDmis(True)) \
        .grid(column=1, row=0, sticky=tk.NSEW, padx=5, pady=5)
        tk.Button(baseBox, text='打开默认输出目录', command=self.onOpenDefaultDataDir) \
        .grid(column=2, row=0, sticky=tk.NSEW, padx=5, pady=5)
        tk.Button(baseBox, text='打开测量程序所在的位置', command=self.onOpenProgramFile) \
        .grid(column=3, row=0, sticky=tk.NSEW, padx=5, pady=5)

        # 序列号工具组框
        row += 1
        snBox = tk.LabelFrame(tabFrame, text='序列号工具', padx=10, pady=10)
        snBox.grid(column=0, row=row, columnspan=4, sticky=tk.NSEW)
        for i in range(4):
            snBox.grid_columnconfigure(i, weight=1)
        # 组框内部组件：
        tk.Button(snBox, text='添加序列号输入', command=self.onAddInputSN) \
        .grid(column=0, row=0, sticky=tk.NSEW, padx=5, pady=5)
        self.isForceEnMode = tk.BooleanVar(self, value=True)
        tk.Checkbutton(snBox, text='强制切换英语键盘输入', variable=self.isForceEnMode, command=self.onUpdate) \
        .grid(column=1, row=0, sticky=tk.W)
        tk.Label(snBox, text='注：插入位置在活动光标后') \
        .grid(column=2, row=0, sticky=tk.W)
        tk.Button(snBox, text='移除序列号输入', command=self.onRemoveInputSN) \
        .grid(column=3, row=0, sticky=tk.NSEW, padx=5, pady=5)

        # 导出工具组框
        row += 1
        exportBox = tk.LabelFrame(tabFrame, text='导出工具', padx=10, pady=10)
        exportBox.grid(column=0, row=row, columnspan=4, sticky=tk.NSEW)
        for i in range(4):
            exportBox.grid_columnconfigure(i, weight=1)
        # 组框内部组件：
        cRow = 0
        self.fileOptionVar = tk.IntVar(self, value=MainUI.FileOptions.NOSPECIFIED)
        tk.Radiobutton(exportBox, text='默认目录', variable=self.fileOptionVar, value=MainUI.FileOptions.NOSPECIFIED, command=self.onUpdate) \
        .grid(column=0, row=cRow, sticky=tk.W)
        # ---
        cRow += 1
        tk.Radiobutton(exportBox, text='指定目录', variable=self.fileOptionVar, value=MainUI.FileOptions.DIRECTORY, command=self.onUpdate) \
        .grid(column=0, row=cRow, sticky=tk.W)
        self.outputDirVar = tk.StringVar(self, value='')
        tk.Entry(exportBox, textvariable=self.outputDirVar, state='readonly', font=("Arial", 10), bd=2) \
        .grid(column=1, row=cRow, columnspan=2, sticky=tk.NSEW, padx=5, pady=5)
        tk.Button(exportBox, text='选择输出目录', command=self.onSelectOutputDir) \
        .grid(column=3, row=cRow, sticky=tk.NSEW, padx=5, pady=5)
        # ---
        cRow += 1
        tk.Radiobutton(exportBox, text='指定文件', variable=self.fileOptionVar, value=MainUI.FileOptions.FILE, command=self.onUpdate) \
        .grid(column=0, row=cRow, sticky=tk.W)
        self.outputFileVar = tk.StringVar(self, value='')
        tk.Entry(exportBox, textvariable=self.outputFileVar, state='readonly', font=("Arial", 10), bd=2) \
        .grid(column=1, row=cRow, columnspan=2, sticky=tk.NSEW, padx=5, pady=5)

        selectFileButton = tk.Menubutton(exportBox, text='选择输出文件 ▾', relief=tk.SOLID, bd=1)
        selectFileButton.grid(column=3, row=cRow, sticky=tk.NSEW, padx=5, pady=5)
        menu = tk.Menu(selectFileButton, tearoff=0)
        menu.add_command(label="📁 新建文件导出（覆盖/新建）", command=lambda: self.onSelectOutputFile())
        menu.add_command(label="📝 追加到已有文件（支持只读文件）", command=lambda: self.onSelectOutputFile(True))
        selectFileButton['menu'] = menu

        cRow += 1
        tk.Button(exportBox, text='添加本工具', command=self.onAddCmd) \
        .grid(column=0, row=cRow, sticky=tk.NSEW, padx=5, pady=5)
        self.isSaveProg = tk.BooleanVar(self, value=True)
        tk.Checkbutton(exportBox, text='保存测量程序副本', variable=self.isSaveProg, command=self.onUpdate) \
        .grid(column=1, row=cRow, sticky=tk.W)
        self.isExportPdf = tk.BooleanVar(self, value=False)
        tk.Checkbutton(exportBox, text='保存PDF报告', variable=self.isExportPdf, command=self.onUpdate) \
        .grid(column=2, row=cRow, sticky=tk.W)
        tk.Button(exportBox, text='移除本工具', command=self.onRemoveTool) \
        .grid(column=3, row=cRow, sticky=tk.NSEW, padx=5, pady=5)

        # 辅助工具组框
        row += 1
        auxiliaryBox = tk.LabelFrame(tabFrame, text='辅助工具', padx=10, pady=10)
        auxiliaryBox.grid(column=0, row=row, columnspan=4, sticky=tk.NSEW)
        for i in range(4):
            auxiliaryBox.grid_columnconfigure(i, weight=1)

        cRow = 0
        tk.Button(auxiliaryBox, text='读取所有命令信息', command=self.onReadAllCmds) \
        .grid(column=0, row=cRow, sticky=tk.NSEW, padx=5, pady=5)
        tk.Button(auxiliaryBox, text='同步PDF属性时间', command=self.onSyncPdfTime) \
        .grid(column=1, row=cRow, sticky=tk.NSEW, padx=5, pady=5)

    def onSyncPdfTime(self):
        filePaths = filedialog.askopenfilenames(
            title="请选择要同步时间的 PDF 文件",
            filetypes=[("PDF 文件", "*.pdf;*.PDF")]
        )
        
        if not filePaths:
            return
            
        totalCount = len(filePaths)
        successCount = 0
        
        for path in filePaths:
            timeTuple = pdftimeprocessor.extractTimeFields(path)
            
            if timeTuple is None:
                continue
                
            if pdftimeprocessor.modifyFileTimeFromTuple(path, timeTuple):
                successCount += 1
                
        infoMessage = f"本次共选择 {totalCount} 个文件\n成功同步修改 {successCount} 个文件"
        self.writeCmdText(infoMessage, False)
        self.update_idletasks()
        self.master.after(2000, self.onUpdate)

    def onReadAllCmds(self):
        self.writeCmdText('正在读取测量程序中的所有命令信息......', False)
        self.update_idletasks()
        pd = PcdmisTools()
        if pd.connectPcDmis() == False:
            self.onUpdate()
            return
        allCmds = pd.readAllCmds()
        if allCmds is None:
            self.onUpdate()
            return
        self.textToClipboard(allCmds)
        self.writeCmdText('信息已写入剪贴板......', False)
        self.update_idletasks()
        self.master.after(2000, self.onUpdate)
    
    def onOpenDefaultDataDir(self):
        dir = constants.Path.defaultDataPath
        try:
            os.makedirs(dir, exist_ok=True)
        except Exception as e:
            errorMsg = traceback.format_exc()
            logging.error(errorMsg)
            TopMessagebox.show('错误', str(e), TopMessagebox.ERROR)
            return
        os.startfile(dir)

    def onOpenProgramFile(self):
        pd = PcdmisTools()
        if pd.connectPcDmis() == False:
            return
        programFilePath = pd.getProgramFullName()
        if os.path.exists(programFilePath):
            subprocess.run(['explorer.exe', '/select,', programFilePath])
        else:
            TopMessagebox.show('错误', '未找到测量程序文件', TopMessagebox.ERROR)

    def onSelectOutputDir(self):
        path = filedialog.askdirectory(title='选择输出路径')
        if path != '':
            path = os.path.normpath(path)
            self.outputDirVar.set(path)
            self.fileOptionVar.set(MainUI.FileOptions.DIRECTORY)
            self.onUpdate()

    def onSelectOutputFile(self, isAppend: bool = False):
        """
        选择输出文件路径
        
        Args:
            isAppend (bool): 
                - False (默认): 新建/保存模式
                - True: 追加模式
        """
        if isAppend:
            path = filedialog.askopenfilename(
                title='选择要追加数据的已有文件',
                filetypes=[('Excel 工作簿', '*.xlsx'), ('所有文件', '*.*')]
            )
        else:
            path = filedialog.asksaveasfilename(
                title='选择或新建输出文件',
                defaultextension='.xlsx',
                filetypes=[('Excel 工作簿', '*.xlsx')],
                confirmoverwrite=False
            )
        
        if path != '':
            path = os.path.normpath(path)
            self.outputFileVar.set(path)
            self.fileOptionVar.set(MainUI.FileOptions.FILE)
            self.onUpdate()

    def onNoOutputPath(self):
        self.outputDirVar.set('')

    def onRemoveInputSN(self):
        self.writeCmdText('正在移除......', False)
        self.update_idletasks()
        pd = PcdmisTools()
        if pd.connectPcDmis() == False:
            self.onUpdate()
            return
        pd.removeInputCommentAndSN()
        self.master.after(100, self.onUpdate)

    def onAddInputSN(self):
        pd = PcdmisTools()
        if pd.connectPcDmis() == False:
            self.onUpdate()
            return
        pd.addInputCommentAndSN(self.isForceEnMode.get())
    
    def onRemoveTool(self):
        """
        删除命令按钮事件回调
        """
        self.writeCmdText('正在移除......', False)
        self.update_idletasks()
        PcdmisTools.connectPcDmis()
        if PcdmisTools.removeTool() == False:
            self.onUpdate()
            return
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
            text = constants.Path.executableCommandString + ' ' + text
        self.cmdText.insert('1.0', text)
        self.cmdText.config(state='disabled')

    def textToClipboard(self, text: str):
        self.master.clipboard_clear()
        self.master.clipboard_append(text)
        self.master.update()

    def onCopyButton(self):
        """
        复制按钮事件回调
        """
        textValue = self.cmdText.get('1.0', 'end').strip()
        self.textToClipboard(textValue)
        self.writeCmdText('已复制', False)
        self.master.after(1000, self.onUpdate)

    def onUpdate(self, *args):
        """
        文件选项单选按钮事件回调
        """
        fileOption = self.fileOptionVar.get()
        if fileOption == MainUI.FileOptions.NOSPECIFIED:
            text = '-n'
        elif fileOption == MainUI.FileOptions.DIRECTORY:
            text = f'-d "{self.outputDirVar.get().strip()}"'
        elif fileOption == MainUI.FileOptions.FILE:
            text = f'-f "{self.outputFileVar.get().strip()}"'
        else:
            TopMessagebox.show('错误', '未知的文件选项', TopMessagebox.ERROR)

        if self.isExportPdf.get():
            text += ' --export-pdf'
        self.writeCmdText(text)
        self.update_idletasks()

    def onAddCmd(self):
        """
        向 PC-DMIS 中添加外部命令
        """
        outputPath = self.outputDirVar.get().strip()

        PcdmisTools.connectPcDmis()
        PcdmisTools.addWarningComment()
        if self.isExportPdf.get():
            PcdmisTools.addPdfPathVar()
        if not self.isSaveProg.get():
            PcdmisTools.addNoSaveProgFlag()
        else:
            PcdmisTools.addNoSaveProgFlag(False)
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
        fileGroup.add_argument('-n', action='store_true', help='不指定导出目录（默认工具目录下data文件夹中）')
        fileGroup.add_argument('-d', '--directory', type=str, help='指定导出目录')
        fileGroup.add_argument('-f', '--file', type=str, help='指定导出文件')

        parser.add_argument('-ep', '--export-pdf', action='store_true', help='导出PDF')

        # 该参数已废弃，无实际作用。保留参数是为了兼容已添加到测量程序中的命令不会发生报错。新控制方法为测量程序中添加 NO_SAVE_PROG="1" 标记。
        parser.add_argument('-np', '--no-prog', action='store_true', help='不保存测量程序文件')

        return parser.parse_args()
    
    @staticmethod
    def cmdMode():
        args = Application.argumentParser()
        outputDir = args.directory
        outputFile = args.file
        try:
            if outputFile is not None:
                outputFile = outputFile.strip()
                outputFileDir = os.path.dirname(outputFile)
                os.makedirs(outputFileDir, exist_ok=True)
                outputDir = ''
            elif outputDir is not None:
                outputDir = outputDir.strip()
                os.makedirs(outputDir, exist_ok=True)
                outputFile = ''
            else:
                outputDir = ''
                outputFile = ''
        except Exception as e:
            outputDir = ''
            outputFile = ''
        PcdmisTools.connectPcDmis(online=True)
        noSaveProg = PcdmisTools.getNoSaveProgFlag()
        dataprocessor.convertPcdCsvToExcel(outputDir=outputDir, outputFile=outputFile, noProg=noSaveProg, exportPdf=args.export_pdf)

    @staticmethod
    def uiMode():
        master = tk.Tk()
        master.attributes('-topmost', True)

        master.title(constants.Basic.projectName)

        width = 756
        height = 540
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
    filename= os.path.join(constants.Path.enterDir, 'error.log'),
    level=logging.ERROR,  # 仅记录 ERROR 及以上级别的日志
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    encoding='utf-8'
)