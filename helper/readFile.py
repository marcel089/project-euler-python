# ==============================================================================
# title           : radFile.py
# description     : Helper for file reading
# author          : Marcel
# date            : 2022-07-19
# version         : 1.0
# python_version  : 3.10.5
# ==============================================================================
from array import array
from time import *


def readIntIntoList(name):
    with open(name) as file:
        # Read all lines into a list. All elements are strings
        data = file.read().splitlines()
        # Change type of all elements of the list into int
        data = map(int, data)
        # Map objects are not readable, convert into list
        data = list(data)
        return data
