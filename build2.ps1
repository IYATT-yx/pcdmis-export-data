$startTime = Get-Date

python -m venv venv
$venvPython = ".\venv\Scripts\python.exe"

& $venvPython -m pip install -r requirements.txt
& $venvPython -m pip install nuitka==4.1.2

$env:NUITKA_CACHE_DIR = Join-Path $PSScriptRoot ".nuitka-cache"
New-Item -ItemType Directory -Force -Path $env:NUITKA_CACHE_DIR | Out-Null

# 编译 ForceEnMode（使用 Nuitka 缓存的 gcc）
$forceEnModeExe = ".\ForceEnMode\x64\Release\ForceEnMode.exe"
if (-not (Test-Path $forceEnModeExe)) {
    $gccPath = Get-ChildItem "$env:NUITKA_CACHE_DIR\downloads\gcc" -Recurse -Filter "g++.exe" -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($gccPath) {
        Write-Output "正在编译 ForceEnMode..."
        $outDir = ".\ForceEnMode\x64\Release"
        New-Item -ItemType Directory -Force -Path $outDir | Out-Null
        & $gccPath.FullName -static -municode -mwindows -o "$outDir\ForceEnMode.exe" ".\ForceEnMode\main.cpp" 2>&1 | Out-Null
        if ($LASTEXITCODE -eq 0) {
            Write-Output "ForceEnMode 编译成功。"
        } else {
            Write-Warning "ForceEnMode 编译失败，将跳过打包。"
        }
    } else {
        Write-Warning "未找到 gcc，ForceEnMode 暂不可编译。首次运行 Nuitka 完成 gcc 下载后，下次构建将自动编译。"
    }
}

& $venvPython .\savebuildtime.py

$dataFileArgs = @(
    "--standalone",
    "--windows-uac-admin",
    "--windows-console-mode=disable",
    "--lto=yes",
    "--no-deployment-flag=self-contained",
    "--enable-plugin=tk-inter",
    "--windows-company-name=IYATT-yx",
    "--windows-product-name=PC-DMIS 数据导出工具",
    "--windows-file-description=PC-DMIS 测量数据自动化导出程序",
    "--windows-product-version=1.0.0.0",
    "--windows-file-version=1.0.0.0",
    "--copyright=Copyright (C) 2026 IYATT-yx. All Rights Reserved.",
    "--windows-icon-from-ico=.\icon.ico",
    "--include-data-file=.\icon.ico=.\",
    "--include-data-file=.\PcdDimToCsvExporter.bas=.\"
)

if (Test-Path $forceEnModeExe) {
    $dataFileArgs += "--include-data-file=$forceEnModeExe=.\"
} else {
    Write-Warning "ForceEnMode.exe 不存在，跳过打包。"
}

$dataFileArgs += @(
    "--output-dir=dist",
    "--output-filename=pcdmis-export-data_win_amd64",
    ".\pcdmis-export-data.py"
)

& $venvPython -m nuitka @dataFileArgs

$endTime = Get-Date
$elapsedTime = New-TimeSpan -Start $startTime -End $endTime
Write-Output "程序构建用时：$($elapsedTime.TotalSeconds) 秒"