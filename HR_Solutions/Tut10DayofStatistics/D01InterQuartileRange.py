/!/bin/python3

# The interquartile range of an array is the difference between 
# its first (Q1) and third (Q3) quartiles (i.e., Q3 - Q1).

# Given an array, values, of  integers and an array, freqs, representing the 
# respective frequencies of values's elements, construct a data set, S, 
# where each value[i] occurs at frequency freqs[i]. Then calculate and 
# print S's interquartile range, rounded to a scale of 1 decimal 
# place (i.e., 12.3 format).

# Tip: Be careful to not use integer division when averaging the 
# middle two elements for a data set with an even number of elements,
#  and be sure to not include the median in your upper and lower 
# data sets.


import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def median(arr):
        m = len(arr)
        if m % 2 == 0:
            return (arr[m // 2 - 1] + arr[m // 2]) / 2
        else:
            return arr[m // 2]
        
def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    data = []
    for value, freq in zip(values, freqs):
        data.extend([value] * freq)
    data.sort()
    n = len(data)
    
    q1 = median(data[:n // 2])
    q3 = median(data[(n + 1) // 2:])
    inter_quartile_range = q3 - q1
    print(f"{inter_quartile_range:.1f}")

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
