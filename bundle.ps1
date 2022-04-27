Copy-Item "target/debug/rslib.dll" .
pyinstaller main.py --onefile
