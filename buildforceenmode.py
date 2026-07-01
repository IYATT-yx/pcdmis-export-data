"""
file: buildForceEnMode.py
description: Nuitka 插件，用于构建 ForceEnMode 工具
author: IYATT-yx
copyright:  Copyright (c) 2026 IYATT-yx.
            Licensed under the MIT License. See LICENSE file in the project root for full license information.
"""
import constants

import os
import sys
import subprocess
from nuitka.plugins.PluginBase import NuitkaPluginBase

# ==============================================================================
print("====================================================")
print("★ [User Plugin] 开始编译 ForceEnMode ......")

cppSource = os.path.join(constants.Path.runtimeDir, "ForceEnMode", "main.cpp")
binDir = os.path.join(constants.Path.runtimeDir, "bin")
outputExePath = os.path.join(binDir, "ForceEnMode.exe")

os.makedirs(binDir, exist_ok=True)

if not os.path.exists(cppSource):
    print(f"❌ 错误：未找到 C++ 源文件 {cppSource}")
    sys.exit(1)

compilerPath = None
vcVarsAllBat = None
programFiles = os.environ.get("ProgramFiles(x86)", "C:\\Program Files (x86)")
vsWherePath = os.path.join(programFiles, "Microsoft Visual Studio", "Installer", "vswhere.exe")

if os.path.exists(vsWherePath):
    vsWhereCmd = f'"{vsWherePath}" -latest -products * -requires Microsoft.VisualStudio.Component.VC.Tools.x86.x64 -property installationPath'
    res = subprocess.run(vsWhereCmd, shell=True, capture_output=True, text=True)
    vsPath = res.stdout.strip()
    
    if vsPath:
        vcVarsAllBat = os.path.join(vsPath, "VC", "Auxiliary", "Build", "vcvarsall.bat")
        hostArch = "HostX64" if "64" in os.environ.get("PROCESSOR_ARCHITECTURE", "") else "HostX86"
        toolsPath = os.path.join(vsPath, "VC", "Tools", "MSVC")
        if os.path.exists(toolsPath):
            versions = sorted(os.listdir(toolsPath), reverse=True)
            if versions:
                compilerPath = os.path.join(toolsPath, versions[0], "bin", hostArch, "x64", "cl.exe")

if not compilerPath or not os.path.exists(compilerPath):
    print("❌ 错误：未能通过 vswhere 探测到有效的 MSVC cl.exe 路径！")
    sys.exit(1)

vsFlags = [
    "/nologo",
    "/std:c++23",          # 预览版 C++23 标准
    "/O2",                 # 最大速度优化
    "/GL",                 # 全程序优化
    "/EHsc",               # 严谨异常捕获
    "/MD",                 # 使用多线程动态运行时库
    "/utf-8",
    "/Zc:wchar_t",         # 强制 wchar_t 为内置类型
    "/permissive-",        # 强化标准符合性，关闭滞后扩展
    '/D "NDEBUG"',
    '/D "_CONSOLE"',
    '/D "UNICODE"',
    '/D "_UNICODE"'
]

flagsStr = " ".join(vsFlags)

if vcVarsAllBat and os.path.exists(vcVarsAllBat):
    cmd = f'"{vcVarsAllBat}" x64 && "{compilerPath}" {flagsStr} "{cppSource}" /Fe"{outputExePath}" user32.lib'
else:
    cmd = f'"{compilerPath}" {flagsStr} "{cppSource}" /Fe"{outputExePath}" user32.lib'

print(f"★ [User Plugin] 执行 MSVC 构建命令:\n{cmd}")
result = subprocess.run(cmd, shell=True, env=os.environ, cwd=constants.Path.runtimeDir, capture_output=True, text=True)

if result.returncode == 0:
    print("★ [User Plugin] ForceEnMode.exe 编译成功！")
else:
    print(f"❌ 编译器输出错误日志:\n{result.stderr}\n{result.stdout}")
    sys.exit(1)
print("====================================================")

class BuildForceEnMode(NuitkaPluginBase):
    plugin_name = __name__.split(".")[-1]
