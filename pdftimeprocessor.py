"""
file: pdftimeprocessor.py
description: 处理 PDF 文件时间
author: IYATT-yx
copyright:  Copyright (c) 2025-2026 IYATT-yx.
            Licensed under the MIT License. See LICENSE file in the project root for full license information.
"""
from topmessagebox import TopMessagebox

from pathlib import Path
import re
import os
import datetime
import pywintypes
import win32file
import win32con

def extractTimeFields(filePath) -> tuple[int, int, int, int, int, int] | None:
    """
    提取文件名中的时间字段

    Args:
        filePath (str): 文件路径

    Returns:
        tuple: (年, 月, 日, 时, 分, 秒)
    """
    mainName = Path(filePath).stem
    
    pattern = r".*\((\d{8})_(\d{6})\)$"
    match = re.match(pattern, mainName)
    
    if match:
        dateStr = match.group(1)
        timeStr = match.group(2)
        
        return (
            int(dateStr[0:4]),  # 年
            int(dateStr[4:6]),  # 月
            int(dateStr[6:8]),  # 日
            int(timeStr[0:2]),  # 时
            int(timeStr[2:4]),  # 分
            int(timeStr[4:6])   # 秒
        )
    else:
        return None
        
def modifyFileTimeFromTuple(filePath: str, timeTuple: tuple) -> bool:
    """
    根据传入的时间元组修改文件的三个属性时间

    Args:
        filePath (str): 文件路径
        timeTuple (tuple): 时间元组 (年, 月, 日, 时, 分, 秒)

    Returns:
        bool: 修改成功返回 True，否则返回 False
    """
    if not timeTuple or len(timeTuple) != 6:
        TopMessagebox.show("错误", "时间元组格式错误", TopMessagebox.ERROR)
        return False
        
    year, month, day, hour, minute, second = timeTuple
    targetDt = datetime.datetime(year, month, day, hour, minute, second)
    win32Time = pywintypes.Time(targetDt)
    
    try:
        handle = win32file.CreateFile(
            filePath,
            win32con.GENERIC_WRITE,
            win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
            None,
            win32con.OPEN_EXISTING,
            0,
            None
        )
        
        win32file.SetFileTime(
            handle,
            CreationTime=win32Time,
            LastAccessTime=win32Time,
            LastWriteTime=win32Time,
            UTCTimes=False
        )
        
        handle.close()
        print(f"[TimeModule] 成功！已将文件 {os.path.basename(filePath)} 的三时统一修改为: {targetDt}")
        return True
        
    except Exception as e:
        print(f"[TimeModule] 写入时间失败: {e}")
        return False