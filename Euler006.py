# ==============================================================================
# title           : Euler006.py
# description     : https://projecteuler.net/problem=6
# author          : Marcel
# date            : 2022-07-17
# version         : 1.0
# python_version  : 3.10.5
# ==============================================================================

from time import *

def solve():
    zahl = 0
    zahl2 = 0
    i = 0

    while i <= 100:
        zahl += i * i
        zahl2 = zahl2 + i
        i += 1

    print(zahl2 * zahl2 - zahl)

t1 = time()
solve()
t2 = time()

print('Running for: ', round(t2 - t1, 4), 'sec')