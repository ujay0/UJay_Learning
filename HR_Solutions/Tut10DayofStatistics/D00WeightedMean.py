#!/bin/python3

# Task
# Given an array, X, of N integers and an array, W, representing the 
# respective weights of X's elements, calculate and print the weighted 
# mean of X's elements. Your answer should be rounded to a scale of 1 decimal place (i.e., 12.3 format).


import math
import os
import random
import re
import sys

#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
#

# Example
# The array of values X = [1, 2, 3] and their respective weights W = [5, 10, 15]. 
# Their sum is 1*5 + 2*10 + 3*15 = 5 + 20 + 45 = 70. The sum of weights 
# is 5 + 10 + 15 = 30. The weighted mean is 70 / 30 = 2.3. Print 2.3 and return.

def weightedMean(X, W):
    # Write your code here
    sum_weighted = 0
    weights_sum = 0
    result = 0
    for i in range(len(X)):
        sum_weighted += X[i] * W[i]
        weights_sum += W[i]
    result = round(sum_weighted / weights_sum, 1)
    return result


if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    # weightedMean(vals, weights)
    print(weightedMean(vals, weights))

