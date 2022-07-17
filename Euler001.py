# ==============================================================================
# title           : Euler001.py
# description     : https://projecteuler.net/problem=1
# author          : Marcel
# date            : 2022-07-17
# version         : 1.0
# python_version  : 3.10.5
# ==============================================================================

from time import *

def solve():
    i = 0
    y = 0

    while i < 1000:
        if (i % 3 == 0) or (i % 5 == 0) :
            y = y + i
        i += 1

    print (y)

t1 = time()
solve()
t2 = time()

print('Running for: ', round(t2 - t1, 4), 'sec')