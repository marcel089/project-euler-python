# ==============================================================================
# title           : Euler004.py
# description     : https://projecteuler.net/problem=4
# author          : Marcel
# date            : 2022-07-17
# version         : 1.0
# python_version  : 3.10.5
# ==============================================================================

from time import *

def solve():
    x = 999
    y = 999
    z = 0

    while x > 1:
        if str(x * y) == str(x * y)[::-1]:
            if z < x * y:
                z = x * y
            break
        else:
            while y >= x:
                if str(x * y) == str(x * y)[::-1]:
                    if z < x * y:
                        z = x * y
                    break
                y -= 1
        x -= 1
        y = 999

    print(z)

t1 = time()
solve()
t2 = time()

print('Running for: ', round(t2 - t1, 4), 'sec')
