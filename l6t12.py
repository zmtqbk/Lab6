import string

def genfiles():
    for letter in string.ascii_uppercase:
        filename = f"{letter}.txt"
        try:
            with open(filename, 'w') as file:
                file.write(f"ths is file {filename}")
            print(f"file {filename} created")
        except Exception as e:
            print(f"error occured {e}")

genfiles()