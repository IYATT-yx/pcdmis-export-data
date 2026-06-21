"""
file: pcdmistools.py
description: PC-DMIS 工具类。连接 PC-DMIS、插入 BASIC 脚本和外部命令
author: IYATT-yx
copyright:  Copyright (c) 2025-2026 IYATT-yx.
            Licensed under the MIT License. See LICENSE file in the project root for full license information.
"""
from obtype import Obtype
from enumfieldtypes import EnumFieldTypes
import constants
import os

import win32com.client as wc
import pywintypes
from tkinter import messagebox

class PcdmisTools:
    cmds = None

    @staticmethod
    def connectPcDmis(save: bool = False):
        """
        连接 PC-DMIS

        Args:
            save (bool, optional): 是否保存测量程序. Defaults to False.
        """
        try:
            app = wc.Dispatch('PCDLRN.Application')
        except pywintypes.com_error as e:
            if e.hresult == -2147221021 or e.hresult == -2146959355:
                raise RuntimeError('请确保PC-DMIS已经以管理员身份运行')
            else:
                raise RuntimeError(f'连接 PC-DMIS 失败：{str(e)}')
        part = app.ActivePartProgram
        PcdmisTools.cmds = part.Commands
        if save:
            part.Save
    
    @staticmethod
    def addBasicAndExternalCommand(commandString: str):
        """
        将本工具插入到测量程序末尾

        Args:
            commandString (str): 外部命令字符串
        """
        if PcdmisTools.cmds is None:
            messagebox.showerror('错误', '未连接 PC-DMIS')
            return
        
        endCmd = PcdmisTools.cmds. LastCommand
        PcdmisTools.cmds.InsertionPointAfter(endCmd)

        basicPath = os.path.join(constants.Path.programFileDir, 'PcdDimToCsvExporter.bas')
        cmd = PcdmisTools.cmds.Add(Obtype.BASIC_SCRIPT, True)
        cmd.PutText(basicPath, EnumFieldTypes.FILE_NAME, 0)
        cmd.PutText('是', EnumFieldTypes.SHOW_DETAILS, 0)
        cmd.PutText('Main', EnumFieldTypes.SUB_NAME, 0)
        cmd.Marked = True 

        cmd = PcdmisTools.cmds.Add(Obtype.EXTERNAL_COMMAND, True)
        cmd.PutText(commandString, EnumFieldTypes.COMMAND_STRING, 0)
        cmd.PutText('不显示', EnumFieldTypes.DISPLAY_TRACE, 0)
        cmd.PutText('等待', EnumFieldTypes.TRACE_NAME, 0)

    @staticmethod
    def removeCommand():
        """
        采用倒序遍历方式移除命令，彻底规避塌陷引起的索引错乱
        """
        if PcdmisTools.cmds is None:
            messagebox.showerror('错误', '未连接 PC-DMIS')
            return

        for idx in range(PcdmisTools.cmds.Count - 1, -1, -1):
            cmd = PcdmisTools.cmds[idx]
            if cmd is None:
                continue

            if cmd.Type == Obtype.BASIC_SCRIPT:
                basicFileName = cmd.GetFieldValue(EnumFieldTypes.FILE_NAME, 0)
                if 'PcdDimToCsvExporter'.upper() in basicFileName.upper():
                    cmd.Remove()
            elif cmd.Type == Obtype.END_SCRIPT:
                cmd.Remove()
            elif cmd.Type == Obtype.EXTERNAL_COMMAND:
                extCmdStr = cmd.GetFieldValue(EnumFieldTypes.COMMAND_STRING, 0)
                if 'pcdmis-export-data'.upper() in extCmdStr.upper():
                    cmd.Remove()
