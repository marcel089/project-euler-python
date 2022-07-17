# ==============================================================================
# title           : Euler009.py
# description     : https://projecteuler.net/problem=9
# author          : Marcel
# date            : 2022-07-17
# version         : 1.0
# python_version  : 3.10.5
# ==============================================================================

from time import *

def solve():
    a = 100
    while a < 500:
        b = a + 1
        while b < 500:
            c = b + 1
            while c < 500:
                if (a * a + b * b == c * c) and (a + b + c == 1000):
                    print('a = {}, b = {}, c = {}, abc = {}'.format(a, b, c, a * b * c))
                    b = 500
                    a = 500
                    break
                c += 1
            b += 1
        a += 1

t1 = time()
solve()
t2 = time()

print('Running for: ', round(t2 - t1, 4), 'sec')

