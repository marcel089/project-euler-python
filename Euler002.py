# ==============================================================================
# title           : Euler002.py
# description     : https://projecteuler.net/problem=2
# author          : Marcel
# date            : 2022-07-17
# version         : 1.0
# python_version  : 3.10.5
# ==============================================================================

from time import *

def solve():
    alt = 1
    neu = 2
    temp = 0
    summe = 0

    while alt < 4000000:
        if alt % 2 == 0:
            summe += alt

        temp = neu
        neu = alt + neu
        alt = temp

    print (summe)

t1 = time()
solve()
t2 = time()

print('Running for: ', round(t2 - t1, 4), 'sec')