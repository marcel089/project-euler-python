# ==============================================================================
# title           : Euler014.py
# description     : https://projecteuler.net/problem=14
# author          : Marcel
# date            : 2022-07-19
# version         : 1.0
# python_version  : 3.10.5
# ==============================================================================

from time import *


def collatz(k):
    n = 0
    # Collatz sequence for 1
    if k == 1:
        n += 1
        return n

    # Collatz sequence for any positiv int
    # Saved in an array
    while k != 1:
        if k % 2 == 0:
            n += 1
            k = int(k / 2)
        else:
            n += 1
            k = int(3 * k + 1)
    return n


def solve(k):
    max = 0
    tmp = 0
    for i in range(1, k):
        tmp = collatz(i)
        if tmp > max:
            max = tmp
            print('Longest Collatz sequence', i)


t1 = time()
solve(1000000)
t2 = time()

print('Running for: ', round(t2 - t1, 4), 'sec')
