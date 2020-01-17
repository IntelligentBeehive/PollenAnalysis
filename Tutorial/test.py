import math
import time
import threading
import logging


def format_time(sec):
    day = 86400
    hour = 3600
    minute = 60
    return f'{int(sec / day)} days, {int(math.fmod(sec / hour, day))}:{int(math.fmod(sec / minute, hour))}:{int(math.fmod(sec, minute))}'


def iterative_approach():
    timer = time.time()
    e = 1
    b = 1
    for i in range(n):
        if i > 0:
            e = e + 1 / (b * i)
            b = b * i
        if math.fmod(i, 10000) == 0:
            logging.info(f'{int(i / n * 100)}% {format_time(time.time() - timer)}')

# Calculating an approximation of Euler's Number - www.101computing.net/eulers-number

# Method 1: e = limit of (1 + 1/n)^n as n approaches infinity
print("Method 1: e = limit of (1 + 1/n)^n as n approaches infinity")
n = 1000000
e = (1 + 1 / n) ** n
print(e)

# Method 2: Using an infinite series (Iterative approach)
print("\nMethod 2: Using an infinite series (Iterative approach)")
# Complete the code here...
method = threading.Thread(target=iterative_approach, args=(1,))
method.start()
print(e)

# Method 3: Using a continued fraction (Iterative approach)
print("\nMethod 3: Using a continued fraction (Iterative approach)")
# Complete the code here...
