# ==============================================================================
# title           : Euler003.py
# description     : https://projecteuler.net/problem=3
# author          : Marcel
# date            : 2022-07-17
# version         : 1.0
# python_version  : 3.10.5
# ==============================================================================

from time import *

def solve():
    prim = 600851475143
    i = 2

    while prim > 1:
        if prim % i == 0:
            prim = prim / i
            print(i)
        i += 1

t1 = time()
solve()
t2 = time()

print('Running for: ', round(t2 - t1, 4), 'sec')