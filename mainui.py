from pcdmistools import PcdmisTools
from commontools import CommonTools
from dialog import Dialog
from constant import Constant
from customexception import CustomException

import tkinter as tk
from tkinter import ttk
import sys
from tkinter import filedialog
import os

Dialog(Constant.Dialog)

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
        tk.Radiobutton(tabFrame, text='指定目录', variable=self.fileOption, value=MainUI.FileOptions.DIRECTORY, command=self.onFileOptionRadiobutton) \
        .grid(column=0, row=0, sticky=tk.W)
        tk.Radiobutton(tabFrame, text='运行时指定目录', variable=self.fileOption, value=MainUI.FileOptions.SPECIFYDIRECTORYATRUNTIME, command=self.onFileOptionRadiobutton) \
        .grid(column=0, row=1, sticky=tk.W)
        tk.Radiobutton(tabFrame, text='指定文件', variable=self.fileOption, value=MainUI.FileOptions.FILE, command=self.onFileOptionRadiobutton) \
        .grid(column=0, row=2, sticky=tk.W)
        tk.Radiobutton(tabFrame, text='运行时指定文件', variable=self.fileOption, value=MainUI.FileOptions.SPECIFYFILEATRUNTIME, command=self.onFileOptionRadiobutton) \
        .grid(column=0, row=3, sticky=tk.W)
        tk.Radiobutton(tabFrame, text='不指定', variable=self.fileOption, value=MainUI.FileOptions.NOSPECIFIED, command=self.onFileOptionRadiobutton) \
        .grid(column=0, row=4, sticky=tk.W)

        # 目录和文件输入框
        self.directoryEntryValue = tk.StringVar()
        self.fileEntryValue = tk.StringVar()
        tk.Entry(tabFrame, textvariable=self.directoryEntryValue, width=80) \
        .grid(column=1, row=0, sticky=tk.NSEW)
        self.fileEntry = tk.Entry(tabFrame, textvariable=self.fileEntryValue, width=80) \
        .grid(column=1, row=2, sticky=tk.NSEW)

        # 操作按钮
        tk.Button(tabFrame, text='浏览文件夹', command=self.onBrowseFolderButton) \
        .grid(column=2, row=0, sticky=tk.NSEW)
        tk.Button(tabFrame, text='浏览文件', command=self.onBrowseFileButton) \
        .grid(column=2, row=2, sticky=tk.NSEW)
        tk.Button(tabFrame, text='复制命令', command=self.onCopyButton) \
        .grid(column=0, row=5, sticky=tk.NSEW)
        tk.Button(tabFrame, text='添加命令', command=self.onAddCmd) \
        .grid(column=0, row=6, sticky=tk.NSEW)

        # 命令输出框
        self.cmdText = tk.Text(tabFrame, height=5)
        self.cmdText.grid(column=1, row=5, columnspan=2, rowspan=2, sticky=tk.NSEW)

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
            initialdir=CommonTools.getMyPath(),
            title='选择导出目录',
            mustexist=True
        )
        if directory == '':
            Dialog.log('取消选择文件夹', Dialog.INFO)
            return
        self.directoryEntryValue.set(
            os.path.normpath(directory)
        )

    def onBrowseFileButton(self):
        """
        浏览文件按钮事件回调
        """
        file = filedialog.asksaveasfilename(
            initialdir=CommonTools.getMyPath(),
            title='选择导出文件',
            filetypes=[('Excel 工作簿', '*.xlsx')],
            confirmoverwrite=False
        )
        if file == '':
            Dialog.log('取消选择文件', Dialog.INFO)
            return
        self.fileEntryValue.set(
            os.path.normpath(file)
        )

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
        self.cmdText.delete('1.0', 'end')
        if addExePath:
            if CommonTools.getPackagedStatus():
                text = sys.executable + ' ' + text
            else:
                text = sys.executable + ' ' + sys.argv[0] + ' ' + text
        self.cmdText.insert('1.0', text)

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
                raise CustomException('未知选项', CustomException.CRITICAL)

    def onAddCmd(self):
        """
        向 PC-DMIS 中添加外部命令
        """
        PcdmisTools.connect()
        exePath = self.cmdText.get('1.0', 'end').strip()
        PcdmisTools.addExternalCommand(exePath)

    def aboutTabUI(self, tabFrame: ttk.Frame):
        """
        “关于”标签界面
        """
        text = tk.Text(tabFrame)
        text.pack(fill='both')
        text.insert('end', Constant.Basic.description)
        text.config(state='disabled')

def test1():
    """
    基本功能测试
    """
    root = tk.Tk()
    mui = MainUI(root)
    root.mainloop()

if __name__ == '__main__':
    test1()