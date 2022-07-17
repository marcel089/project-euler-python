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
    n = 1
    while True:
        if (n % 19 == 0):
            if (n % 17 == 0):
                if (n % 13 == 0):
                    if (n % 11 == 0):
                        if (n % 7 == 0):
                            if (n % 5 == 0):
                                if (n % 3 == 0):
                                    if (    n %  2 == 0 and n %  4 == 0 
                                        and n %  6 == 0 and n %  8 == 0
                                        and n %  9 == 0 and n % 10 == 0
                                        and n % 12 == 0 and n % 14 == 0
                                        and n % 15 == 0 and n % 16 == 0
                                        and n % 18 == 0 and n % 20 == 0):
             
                                        print(n)
                                        break

        n += 1


t1 = time()
solve()
t2 = time()

print('Running for: ', round(t2 - t1, 4), 'sec')