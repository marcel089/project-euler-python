# ==============================================================================
# title           : Euler012.py
# description     : https://projecteuler.net/problem=12
# author          : Marcel
# date            : 2022-07-19
# version         : 1.0
# python_version  : 3.10.5
# ==============================================================================

import math
from time import *


def divisors(n):
    i = 2
    arr = [1, n]
    # Runs until square of n
    while i <= math.sqrt(n):
        if (n % i == 0):
            # If equal, only add one of them to array
            if (n / i == i):
                arr.append(i)
            else:
                # Otherwise add both
                arr.append(i)
                arr.append(int(n/i))
        i = i + 1
    # Return array with all divisors of n
    return arr


def solve(maxDivisors):
    k = 1
    j = 2
    while (len(divisors(k)) <= maxDivisors):
        k = j + k
        j += 1
    
    print(k)

t1 = time()
solve(500)
t2 = time()

print('Running for: ', round(t2 - t1, 4), 'sec')
