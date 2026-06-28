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
    part = None

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
        PcdmisTools.part = app.ActivePartProgram
        if PcdmisTools.part is None:
            raise RuntimeError('未找到活动测量程序胡或者未运行 PC-DMIS')
        PcdmisTools.cmds = PcdmisTools.part.Commands
        if save:
            PcdmisTools.part.Save
    
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
        
        endCmd = PcdmisTools.cmds.LastCommand
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

    pdfPathVarName = 'PDF_FULL_NAME'

    @staticmethod
    def addPdfPathVar():
        """
        添加PDF导出路径变量
        """
        if PcdmisTools.cmds is None:
            messagebox.showerror('错误', '未连接 PC-DMIS')
            return
        
        endCmd = PcdmisTools.cmds.LastCommand
        PcdmisTools.cmds.InsertionPointAfter(endCmd)

        cmd = PcdmisTools.cmds.Add(Obtype.ASSIGNMENT, True)
        cmd.PutText(PcdmisTools.pdfPathVarName, EnumFieldTypes.DEST_EXPR, 0)
        cmd.PutText('0', EnumFieldTypes.SRC_EXPR, 0)
    
    @staticmethod
    def setPdfPathVar(newVal: str):
        if PcdmisTools.part is None:
            messagebox.showerror('错误', '未连接 PC-DMIS')
            return
        valueObj = PcdmisTools.part.GetVariableValue(PcdmisTools.pdfPathVarName)
        valueObj.StringValue = newVal
        PcdmisTools.part.SetVariableValue(PcdmisTools.pdfPathVarName, valueObj)

    @staticmethod
    def addPrintReport():
        """
        添加打印报告命令
        """
        if PcdmisTools.cmds is None:
            messagebox.showerror('错误', '未连接 PC-DMIS')
            return
        
        endCmd = PcdmisTools.cmds.LastCommand
        PcdmisTools.cmds.InsertionPointAfter(endCmd)

        cmd = PcdmisTools.cmds.Add(Obtype.SET_COMMENT, True)
        cmd.PutText('文档', EnumFieldTypes.COMMENT_TYPE, 0)
        cmd.PutText(f'下方打印报告的文件路径已绑定到变量 ==>> {PcdmisTools.pdfPathVarName}', EnumFieldTypes.COMMENT_FIELD, 0)
        cmd.PutText('否', EnumFieldTypes.OUTPUT_TYPE, 0)

        cmd = PcdmisTools.cmds.Add(Obtype.PRINT_REPORT, True)
        cmd.PutText('终止', EnumFieldTypes.MODE_TYPE, 0)
        cmd.PutText('开', EnumFieldTypes.PRINT_TO_FILE, 0)
        cmd.PutText('覆盖', EnumFieldTypes.FILE_COMMAND_TYPE, 0)
        cmd.SetExpression(PcdmisTools.pdfPathVarName, EnumFieldTypes.FILE_NAME, 0)
        cmd.PutText('PDF', EnumFieldTypes.PRINT_OUTFPUT_FORMAT_TYPE, 0)
        cmd.PutText('是', EnumFieldTypes.RESET_REPORT, 0)
        cmd.PutText('开', EnumFieldTypes.ONOFF_TYPE, 0)
        cmd.PutText('关', EnumFieldTypes.PRINT_TO_PRINTER, 0)
        cmd.PutText('关', EnumFieldTypes.OUTPUT_DMIS_REPORT, 0)
        cmd.PutText('索引', EnumFieldTypes.OVERWRITE,0)
        cmd.PutText('无', EnumFieldTypes.OUTPUT_FEATURE_NOMS, 0)
        cmd.PutText('否', EnumFieldTypes.OUTPUT_FEAT_W_DIMENS, 0)
        cmd.PutText('关', EnumFieldTypes.OUTPUT_TO_REPORT, 0)
        cmd.PutText('删除实例', EnumFieldTypes.PRINT_DELETE_RUNS, 0)

    @staticmethod
    def addInputCommentAndSN(forceEnMode: bool = True):
        if PcdmisTools.cmds is None:
            messagebox.showerror('错误', '未连接 PC-DMIS')
            return
        
        if forceEnMode:
            cmd = PcdmisTools.cmds.Add(Obtype.EXTERNAL_COMMAND, True)
            if constants.Status.packaged:
                forceEnModePath = os.path.join(constants.Path.programFileDir, 'ForceEnMode.exe')
            else:
                forceEnModePath = os.path.join(constants.Path.programFileDir, 'ForceEnMode', 'x64', 'Release', 'ForceEnMode.exe')
            cmd.PutText(forceEnModePath, EnumFieldTypes.COMMAND_STRING, 0)
            cmd.PutText('不显示', EnumFieldTypes.DISPLAY_TRACE, 0)
            cmd.PutText('等待', EnumFieldTypes.TRACE_NAME, 0)
        
        cmd = PcdmisTools.cmds.Add(Obtype.SET_COMMENT, True)
        cmd.PutText('输入', EnumFieldTypes.COMMENT_TYPE, 0)
        cmd.PutText('请输入产品编号：', EnumFieldTypes.COMMENT_FIELD, 0)
        cmd.PutText('是', EnumFieldTypes.OUTPUT_TYPE, 0)
        commentId = str(cmd.ID)

        cmd = PcdmisTools.cmds.Add(Obtype.ASSIGNMENT, True)
        cmd.PutText('SN', EnumFieldTypes.DEST_EXPR, 0)
        cmd.PutText(f'{commentId}.INPUT', EnumFieldTypes.SRC_EXPR, 0)

    @staticmethod
    def removeInputCommentAndSN():
        if PcdmisTools.cmds is None:
            messagebox.showerror('错误', '未连接 PC-DMIS')
            return

        for idx in range(PcdmisTools.cmds.Count - 1, -1, -1):
            cmd = PcdmisTools.cmds[idx]
            if cmd is None:
                continue

            if cmd.Type == Obtype.EXTERNAL_COMMAND:
                extCmdStr = cmd.GetFieldValue(EnumFieldTypes.COMMAND_STRING, 0)
                if 'ForceEnMode'.upper() in extCmdStr.upper():
                    cmd.Remove()
            elif cmd.Type == Obtype.ASSIGNMENT:
                dest = cmd.GetFieldValue(EnumFieldTypes.DEST_EXPR, 0)
                if 'SN' == dest:
                    cmd.Remove()
            elif cmd.Type == Obtype.SET_COMMENT:
                comment = cmd.GetFieldValue(EnumFieldTypes.COMMENT_FIELD, 0)
                if '产品编号' in comment:
                    cmd.Remove()

    @staticmethod
    def removeTool():
        """
        移除本工具
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
                if 'pcdmis-export-data_win_amd64'.upper() in extCmdStr.upper() or 'python.exe' in extCmdStr.lower():
                    cmd.Remove()
            elif cmd.Type == Obtype.ASSIGNMENT:
                dest = cmd.GetFieldValue(EnumFieldTypes.DEST_EXPR, 0)
                if PcdmisTools.pdfPathVarName in dest:
                    cmd.Remove()
            elif cmd.Type == Obtype.SET_COMMENT:
                comment = cmd.GetFieldValue(EnumFieldTypes.COMMENT_FIELD, 0)
                if PcdmisTools.pdfPathVarName in comment:
                    cmd.Remove()
            elif cmd.Type == Obtype.PRINT_REPORT:
                cmd.Remove()
