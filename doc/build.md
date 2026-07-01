# 构建说明

项目使用 Nuitka 打包为独立可执行文件，构建脚本为项目根目录下的 `build.ps1`。

## 前置要求

- Python 3.11
- Windows 10 及以上

## 构建步骤

```powershell
powershell -ExecutionPolicy Bypass -File .\build.ps1
```

脚本会自动完成：
1. 创建 venv 虚拟环境并安装依赖（pywin32、openpyxl）
2. 安装 Nuitka 4.1.2
3. 自动编译 ForceEnMode.exe（使用 Nuitka 缓存的 gcc，无需 Visual Studio）
4. 编译为独立 exe，输出到 `dist\pcdmis-export-data.dist\`

> 首次运行 Nuitka 时会自动下载 gcc 编译器，完成后 ForceEnMode.exe 才能自动编译。若首次构建时 gcc 尚未下载，ForceEnMode 将被跳过，第二次构建即可自动完成。

## 测试环境

- Python 3.11
- Nuitka 4.1.2
- gcc 15.2.0 (MinGW64, Nuitka 自动下载)
- PC-DMIS 生产环境测试版本：2018 R1、2020 R1、2023.1
