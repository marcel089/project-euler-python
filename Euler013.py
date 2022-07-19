# ==============================================================================
# title           : Euler013.py
# description     : https://projecteuler.net/problem=13
# author          : Marcel
# date            : 2022-07-19
# version         : 1.0
# python_version  : 3.10.5
# ==============================================================================

from math import prod
from time import *
from helper.readFile import readIntIntoList


def solve():
    data = readIntIntoList('data/Euler013.txt')

    i = 0
    product = 0
    while i < len(data):
        product += data[i]
        i += 1

    print(str(product)[:10])


t1 = time()
solve()
t2 = time()

print('Running for: ', round(t2 - t1, 4), 'sec')
