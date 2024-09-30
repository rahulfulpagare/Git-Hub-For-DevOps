import os

command = "systeminfo"
print(os.system(command))

def check_cpu(command):
    print(os.system(command))

check_cpu("Get-NetAdapter")