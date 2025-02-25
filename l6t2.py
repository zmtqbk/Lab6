str=input()


def counter(str):
    upper=0
    lower=0

    for char in str:
        if char.isupper():
            upper+=1
        elif char.islower():
            lower+=1

    return upper, lower

up,low = counter(str)

print("upper: ", up)
print("lower: ", low)