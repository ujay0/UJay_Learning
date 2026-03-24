#!/bin/python3
"""
Given a 6x6 2D Array, arr:
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

We define an hourglass in A to be a subset of values with indices falling in this pattern in arr's graphical representation:
a b c
  d
e f g
There are 16 hourglasses in arr, and an hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum.
Input Format
There are 6 lines of input, where each line contains 6 space-separated integers that describe the 2D Array arr.
Constraints
-9 <= arr[i][j] <= 9
Output Format
Print the largest (maximum) hourglass sum found in arr.
Sample Input
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
Sample Output       
19
Explanation
arr contains the following hourglasses:
1 1 1     1 1 0     1 0 0     0 0 0     0 0 0
1 1 1     0 1 0     0 0 0     0 0 0     0 0 0
1 1 1     0 1 0     0 0 0     0 0 0     0 0 0
0 0 2     0 0 4     0 4 4     0 0 0     0 0 0
0 0 0     0 0 0     0 2 0     0 0 0     0 0 0
0 0 1     0 0 2     0 2 4     0 0 0     0 0 0
The hourglass with the maximum sum (19) is:
2 4 4
  2 
1 2 4   

"""
import math
import os
import random
import re
import sys

def get_hourglass_sum(matrix, row, col):
    sum = 0
    sum+= matrix[row - 1][col - 1] 
    sum+= matrix[row - 1][col] 
    sum+= matrix[row - 1][col + 1] 
    sum+= matrix[row][col] 
    sum+= matrix[row + 1][col - 1] 
    sum+= matrix[row + 1][col] 
    sum+= matrix[row + 1][col + 1]
    return sum

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    maxsum=-63;
    for i in range(1,5):
        for j in range (1,5):
            curr_hourglass_sum = get_hourglass_sum(arr, i, j)
            if curr_hourglass_sum > maxsum:
                maxsum=curr_hourglass_sum
    print(maxsum)
