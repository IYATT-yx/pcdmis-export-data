$startTime = Get-Date

python -m venv venv
.\venv\Scripts\Activate.ps1
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
pip install nuitka==4.2

Set-Content -Path ".\buildtime.py" -Value "buildTime = '$(Get-Date -Format 'yyyyMMdd_HHmmss')'" -Encoding UTF8

nuitka --standalone `
--windows-uac-admin `
--windows-console-mode=disable `
--lto=yes `
--no-deployment-flag=self-contained `
--enable-plugin=tk-inter `
--windows-company-name="IYATT-yx" `
--windows-product-name="PC-DMIS 数据导出工具" `
--windows-file-description="PC-DMIS 数据导出工具" `
--windows-product-version="1.0.0.0" `
--windows-file-version="1.0.0.0" `
--copyright="Copyright (C) 2026 IYATT-yx. All Rights Reserved." `
--user-plugin=.\buildforceenmode.py `
--windows-icon-from-ico=.\icon.ico `
--include-data-file=.\icon.ico=.\ `
--include-data-file=.\PcdDimToCsvExporter.bas=.\ `
--include-data-file=.\bin\ForceEnMode.exe=.\ `
--output-dir=dist `
--output-filename=pcdmis-export-data_win_amd64 `
.\pcdmis-export-data.py

if (Test-Path "dist\pcdmis-export-data.dist") {
    if (Test-Path "dist\pcdmis-export-data_win_amd64") {
        Remove-Item -Path "dist\pcdmis-export-data_win_amd64" -Recurse -Force
    }
    Rename-Item -Path "dist\pcdmis-export-data.dist" -NewName "pcdmis-export-data_win_amd64"
}

$endTime = Get-Date
$elapsedTime = New-TimeSpan -Start $startTime -End $endTime
Write-Output "程序构建用时：$($elapsedTime.TotalSeconds) 秒"