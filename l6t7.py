import os
def directs(path):
    return [enrty for enrty in os.listdir(path) if os.path.isdir(os.path.join(path, enrty))]

def files(path):
    return [enrty for enrty in os.listdir(path) if os.path.isfile(os.path.join(path, enrty))]

def all(path):
    return os.listdir(path)

path=input()

directories=directs(path)
print("Directories: " ,directories)

filess=files(path)
print("Files: ", filess)

allll=all(path)
print("All dirs and files: ", allll)