$startTime = Get-Date

python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install nuitka==2.6.4

python .\savebuildtime.py

nuitka --standalone --onefile `
--include-module=pcdlrnconst.pcdlrnconst20232 --include-module=pcdlrnconst.pcdlrnconst2019R2 `
--enable-plugin=tk-inter --windows-icon-from-ico=./icon.ico --include-data-file=./icon.ico=.\ `
--include-data-files=.\icon.ico=.\ `
--output-dir=dist --output-filename=pcdmis-export-data_win_amd64 `
.\pcdmis-export-data.py

$endTime = Get-Date
$elapsedTime = New-TimeSpan -Start $startTime -End $endTime
Write-Output "程序构建用时：$($elapsedTime.TotalSeconds) 秒"