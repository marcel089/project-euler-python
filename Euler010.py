# ==============================================================================
# title           : Euler010.py
# description     : https://projecteuler.net/problem=10
# author          : Marcel
# date            : 2022-07-17
# version         : 1.0
# python_version  : 3.10.5
# ==============================================================================

from time import *

def solve(min, max):
	# Create an Array until with 
	i = 2
	numberArray = [i for i in range(min, max + 1)]

	i = 2
	while i ** 2 <= max:
		if isinstance(numberArray[i], int):
			j = i * 2
			while j < len(numberArray):
				numberArray[j] = False
				j += i
		i += 1
	
	sumPrime = 0
	for i in range (0, len(numberArray)):
		if numberArray[i] != False:
			sumPrime +=  numberArray[i]
	
	# 1 is not a prime number, so it must be removed
	print(sumPrime - 1)
		
t1 = time()
solve(0, 2000000)
t2 = time()

print('Running for: ', round(t2 - t1, 4), 'sec')