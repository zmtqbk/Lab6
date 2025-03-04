def copier(source, dest):
    try:
        with open(source, 'r') as src_file:
            with open(dest, 'w') as dest_file:
                contents=src_file.read()
                dest_file.write(contents)

        print(f"contents havebeen copied from {source} to {dest}")
    except FileNotFoundError:
        print(f"notfound")
    except Exception as e:
        print("error occured")

sourcefile=input("entersource")
destfile=input("wheretogo")

copier(sourcefile, destfile)