#!/bin/python3
# Given an array, a, of size n distinct elements, sort the array in ascending 
# order using the Bubble Sort algorithm above.
#  Once sorted, print the following 3 lines:

# Array is sorted in numSwaps swaps.
# where numSwaps is the number of swaps that took place.
# First Element: firstElement
# where firstElement is the first element in the sorted array.
# Last Element: lastElement
# where lastElement is the last element in the sorted array.
#
#  Hint: To complete this challenge, you will need to add a variable 
# that keeps a running tally of all swaps that occur during execution.


import math
import os
import random
import re
import sys

def sorting(a):
    numberOfSwaps = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j]>a[j+1]:
                temp = a[j]
                a[j]=a[j+1]
                a[j+1]=temp
                numberOfSwaps += 1
    return numberOfSwaps

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    numberOfSwaps = sorting(a)
    # numberOfSwaps = 0
    # for j in range(0,n):
    #     for i in range(0, n-1):
    #         if a[i] > a [i+1]:
    #             a[i]   = a[i] + a[i+1]
    #             a[i+1] = a[i] - a[i+1]
    #             a[i]   = a[i] - a [i+1]
    #             # print(f" a[{i}], a[{i}+1]: {a[i]} , {a[i+1]}") # Checking the swap
    #             numberOfSwaps+=1
    #             if numberOfSwaps == 0:
    #                 break
    
    
    print(f"Array is sorted in {numberOfSwaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[n-1]}")
