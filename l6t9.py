import os

def checker(path):

    if os.path.exists(path):

        directory = os.path.dirname(path)

        filename = os.path.basename(path)
        
        print(f"path exists")
        print(f"Directory: {directory}")
        print(f"Filename: {filename}")
    else:
        print("path does not exist.")

path = input()
checker(path)
