python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install pyinstaller

python .\savebuildtime.py
pyinstaller -F -i .\icon.ico --add-data '.\icon.ico;.' --add-data 'buildTime.txt;.' `
--hidden-import=pcdlrnconst.pcdlrnconst2019R2 --hidden-import=pcdlrnconst.pcdlrnconst20232 `
pcdmis-export-data.py