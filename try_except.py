import sys

try:
    a = 10
    a = a + 'hey'
except Exception as e:
    print(f"Exception Raised : {e}, errorOnLine: {sys.exc_info()[-1].tb_lineno}")