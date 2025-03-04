def tofile(filename, data_list):
    try:
        with open(filename, 'w') as file:
            for item in data_list:
                file.write(f"{item}\n")
        print(f"list went to {filename}")
    except Exception as e:
        print(f"error occured: {e}")

listik=["1", "2", "3", "4"]

namefile="sandar.txt"

tofile(namefile, listik)