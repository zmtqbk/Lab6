import functools

num = [1 ,2 ,3 ,4]

result = functools.reduce(lambda x, y: x * y, num)

print(result)
