#!/bin/python3

# Given an array, arr, of n integers, calculate the respective 
# first quartile (Q1), second quartile (Q2), and third quartile 
# (Q3). It is guaranteed that Q1, Q2, and Q3 are integers.



# Complete the quartiles function in the editor below.
# quartiles has the following parameters:
# int arr[n]: the values to segregate

# int[3]: the medians of the left half of arr,  
# arr in total, and the right half of arr.

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    # Write your code here
    pass

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
