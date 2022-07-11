import sys

try:
    a = 10
    a = a + 'hey'
except Exception as e :
    click.secho(f"Exception Raised : {e}, errorOnLine: {sys.exc_info()[-1].tb_lineno}, file : {os.path.basename(__file__)}", fg="red")
