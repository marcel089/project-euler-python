# ==============================================================================
# title           : Euler011.py
# description     : https://projecteuler.net/problem=11
# author          : Marcel
# date            : 2022-07-17
# version         : 1.0
# python_version  : 3.10.5
# ==============================================================================

from array import array
from time import *

def solve(n):
    with open('Euler011.txt') as file:
        array = file.readlines()
        array = [line.rstrip().split(' ') for line in array]

    x = 0
    y = 0
    i = 0
    j = 0

    sum = array[x][y] + array[x + 1][y] + array[x + 2][y] + array[x + 3][y]
    print (sum)

t1 = time()
solve(4)
t2 = time()

print('Running for: ', round(t2 - t1, 4), 'sec')