# ==============================================================================
# title           : Euler005.py
# description     : https://projecteuler.net/problem=5
# author          : Marcel
# date            : 2022-07-17
# version         : 1.0
# python_version  : 3.10.5
# ==============================================================================

from time import *

def solve():
    zahl = 1
    while True:
        if (zahl % 2 == 0 and
            zahl % 3 == 0 and
            zahl % 4 == 0 and
            zahl % 5 == 0 and
            zahl % 7 == 0 and
            zahl % 8 == 0 and
            zahl % 9 == 0 and
            zahl % 11 == 0 and
            zahl % 12 == 0 and
            zahl % 13 == 0 and
            zahl % 14 == 0 and
            zahl % 16 == 0 and
            zahl % 18 == 0 and
            zahl % 17 == 0 and
            zahl % 19 == 0):

            print(zahl)
            break

        zahl += 1


t1 = time()
solve()
t2 = time()

print('Running for: ', round(t2 - t1, 4), 'sec')