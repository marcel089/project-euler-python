# ==============================================================================
# title           : Euler006.py
# description     : https://projecteuler.net/problem=6
# author          : Marcel
# date            : 2022-07-17
# version         : 1.0
# python_version  : 3.10.5
# ==============================================================================

from time import *

def solve(x):
    m = 0
    n = 0
    i = 1

    while i <= x:
        m += i ** 2
        n += i
        i += 1

    print(n ** 2 - m)

t1 = time()
solve(100)
t2 = time()

print('Running for: ', round(t2 - t1, 4), 'sec')