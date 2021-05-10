pip install pyinstaller

# create exe
pyinstaller --onefile python_code_file.py

# create exe with hidden packages
pyinstaller --hiddenimport win32timezone -F python_code_file.py