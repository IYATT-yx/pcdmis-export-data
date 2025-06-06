$startTime = Get-Date

python -m venv venv
.\venv\Scripts\Activate.ps1
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
pip install nuitka==2.7.0

python .\savebuildtime.py

nuitka --standalone --remove-output --windows-console-mode=disable `
--include-module=pcdlrnconst.pcdlrnconst20232 --include-module=pcdlrnconst.pcdlrnconst2019R2 `
--enable-plugin=tk-inter `
--windows-icon-from-ico=.\icon.ico --include-data-file=.\icon.ico=.\ `
--output-dir=dist --output-filename=pcdmis-export-data_win_amd64 `
.\pcdmis-export-data.py

$endTime = Get-Date
$elapsedTime = New-TimeSpan -Start $startTime -End $endTime
Write-Output "程序构建用时：$($elapsedTime.TotalSeconds) 秒"