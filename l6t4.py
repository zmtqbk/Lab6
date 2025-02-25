import time
import math

num=float(input())
delay=int(input())

def sqafterdelay(num,delay):
    delay_sec=delay/1000

    time.sleep(delay_sec)

    result=math.sqrt(num)
    return result

result=sqafterdelay(num,delay)

print(f"Square root of {num} after {delay} miliseconds is ", result)