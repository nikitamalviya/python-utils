import sys
import datetime

now = datetime.datetime.now()
start_time_import = time.time()

folderconsoleoutput = "console"
if not os.path.exists(folderconsoleoutput):
    os.mkdir(folderconsoleoutput)
console_output = str(now).replace(" ", "_")
console_output = str(now).replace(":", "--")
sys.stdout = open(folderconsoleoutput+"/"+"log_"+console_output+".txt", "w")

print("HELLO")
print("Logs here..")

sys.stdout.close()

