python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install pyinstaller
pyinstaller -F -i .\icon.ico --add-data '.\icon.ico;.' pcdmis-export-data.py