import os

path=input()

def check(path):
    exist=os.path.exists(path)

    read=os.access(path, os.R_OK)

    write=os.access(path, os.W_OK)

    execute=os.access(path, os.X_OK)

    return exist, read, write, execute

exist, read, write, execute = check(path)

if exist:
    print("it exists, readable, writable and executable")

else: 
    print("No")