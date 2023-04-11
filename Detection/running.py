import subprocess
from Detection import data

def check_run():
 cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Description'
 proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
 for line in proc.stdout:
    if line.rstrip():
        data.softwares.append(line.decode().rstrip()) 
        # only print lines that are not empty
        # decode() is necessary to get rid of the binary string (b')
        # rstrip() to remove `\r\n`
       

print(data.softwares)