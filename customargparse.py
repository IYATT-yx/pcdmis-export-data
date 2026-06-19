"""
file: customargparse.py
description: 自定义参数解析器（重写错误方法）
author: IYATT-yx
copyright:  Copyright (c) 2025-2026 IYATT-yx.
            Licensed under the MIT License. See LICENSE file in the project root for full license information.
"""
import argparse

class CustomArgParse(argparse.ArgumentParser):
    def error(self, message):
        raise RuntimeError(f"参数错误：{message}")