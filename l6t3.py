str=input()

def check4pal(str):
    clean=str.replace(" ", "").lower()

    return clean == clean[::-1]

if check4pal(str):
    print("yes bro, its palindrome")

else:
    print("no bro, it isnt")