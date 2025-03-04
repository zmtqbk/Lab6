import os

def delfile(path):
    try:
        if os.path.exists(path):
            if os.access(path, os.W_OK):
                os.remove(path)
                print(f"{path} itsbeendeleted")
            else:
                print(f"notdeleted")
        else:
            print(f"{path} doesnt exist")
    except Exception as e:
        print(f"error occured")

filepath=input("path: ")

delfile(filepath)