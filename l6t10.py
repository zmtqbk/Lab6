import os

path = input("enter the path: ")

def counter(path):
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        return f"The file at {path} was not found."
    except PermissionError:
        return f"Permission denied to access the file at {path}."
    except Exception as e:
        return f"An error occurred: {e}"

linecount = counter(path)

print("num of lines:", linecount)
