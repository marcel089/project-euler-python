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
    for i in range(2, round(math.sqrt(n) + 1)):
        if n % i == 0:  
            return False
    return True

# Finds the value for the given n-th term
def find(max):
    x = 2
    count = 1
    while count <= max:
        if is_prime(x):
            print(x)
            count += 1
        x += 1

t1 = time()
find(10001)
t2 = time()

print('Running for: ', round(t2 - t1, 4), 'sec')