echo 'run "pipenv shell" first'

pyside6-rcc.exe -o ./quant/gui/resources/resource.py ./quant/gui/resources/resource.qrc 

pip install -r requirements.txt

pyinstaller ./quant/main.py -i ./quant/gui/resources/icon/logo.ico