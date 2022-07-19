# ==============================================================================
# title           : Euler016.py
# description     : https://projecteuler.net/problem=16
# author          : Marcel
# date            : 2022-07-19
# version         : 1.0
# python_version  : 3.10.5
# ==============================================================================

from time import *

def solve(k):
    tmp = 2 ** k
    sum = 0
    for digit in str(tmp):
        sum += int(digit)
    
    print (sum)

t1 = time()
solve(1000)
t2 = time()

print('Running for: ', round(t2 - t1, 4), 'sec')
