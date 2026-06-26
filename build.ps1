$startTime = Get-Date

python -m venv venv
.\venv\Scripts\Activate.ps1
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
pip install nuitka==4.1.2

python .\savebuildtime.py

nuitka --standalone `
--remove-output `
--windows-console-mode=disable `
--lto=yes `
--no-deployment-flag=self-contained `
--include-module=pdconst `
--enable-plugin=tk-inter `
--windows-icon-from-ico=.\icon.ico `
--include-data-file=.\icon.ico=.\ `
--include-data-file=.\PcdDimToCsvExporter.bas=.\ `
--include-data-file=.\ForceEnMode\x64\Release\ForceEnMode.exe=.\ `
--output-dir=dist `
--output-filename=pcdmis-export-data_win_amd64 `
.\pcdmis-export-data.py

$endTime = Get-Date
$elapsedTime = New-TimeSpan -Start $startTime -End $endTime
Write-Output "程序构建用时：$($elapsedTime.TotalSeconds) 秒"