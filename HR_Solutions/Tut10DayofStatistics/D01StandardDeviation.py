#!/bin/python3


import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    # Calculate the mean
    mean = sum(arr) / len(arr)
    # Calculate the variance
    variance = sum((x - mean) ** 2 for x in arr) / len(arr)
    # Calculate the standard deviation (square root of variance)
    std_dev = math.sqrt(variance)
    print(f"{std_dev:.1f}")
    return

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
