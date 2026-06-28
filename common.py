"""
file: common.py
description: 功能模块
author: IYATT-yx
copyright:  Copyright (c) 2025-2026 IYATT-yx.
            Licensed under the MIT License. See LICENSE file in the project root for full license information.
"""
import constants

import os

class Common:
    @staticmethod
    def setFileReadOnly(filePath: str, readonly: bool = True):
        """
        设置文件只读

        Params:
            filePath (str): 文件路径
            readonly (bool): 是否只读
        """
        if readonly:
            os.chmod(filePath, 0o444)
        else:
            os.chmod(filePath, 0o777)

    @staticmethod
    def longPath(path: str) -> str:
        """
        将路径转换为长路径

        Params:
            path (str): 路径

        Returns:
            str: 长路径
        """
        path = os.path.normpath(path)
        if not path.startswith("\\\\?\\"):
            # 注意：网络路径（\\Server\Share）要特殊处理
            if path.startswith("\\\\"):
                path = "\\\\?\\UNC" + path[1:]
            else:
                path = "\\\\?\\" + path
        return path