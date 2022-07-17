# ==============================================================================
# title           : Euler007.py
# description     : https://projecteuler.net/problem=7
# author          : Marcel
# date            : 2022-07-17
# version         : 1.0
# python_version  : 3.10.5
# ==============================================================================

import math
from time import *

# Checks if a number is a prime
def is_prime(n):
    count = 0
    for i in range(2, n):
        if n % i == 0:  
            return False
            break
        else:
            count += 1
    if count == n - 2:
        return True


# Finds the value for the given nth term
def term(n):
    x = 0
    count = 0
    while count != n:
        x += 1
        if is_prime(x):
            count += 1
    print(x)


t1 = time()
term(10001)
t2 = time()

print('Running for: ', round(t2 - t1, 4), 'sec')