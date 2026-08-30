# !/bin/python3

# Task
# Given two n-element data sets, X and Y, calculate the value of the Spearman
# rank correlation coefficient.

# Input Format
# The first line contains an integer, n, denoting the size of data sets X and Y.
# The second line contains n space-separated real numbers (scaled to at most one decimal place),
# defining data set X.
# The third line contains n space-separated real numbers (scaled to at most one decimal place),
# defining data set Y.

# Constraints
# 10 <= n <= 100
#  1 < Xi < 100, where Xi is the ith value of data set X.
#  1 < Yi < 100, where Yi is the ith value of data set Y.
# Data set X contains unique values.
# Data set Y contains unique values.
# Output Format
# Print the value of the Spearman rank correlation coefficient, rounded to a scale of 3
# decimal places.

import math
import numpy as np
from scipy.stats import rankdata

# Input data
a = int(input())
# variables to hold the data sets
x = list(map(float, input().split()))
# variables to hold the data sets
y = list(map(float, input().split()))

# rank the data sets
rank_x = rankdata(x, method='max')
# rank the data sets
rank_y = rankdata(y, method='max')

# calculate the difference between the ranks
d = [rank_x[i] - rank_y[i] for i in range(a)]

# calculate the Spearman rank correlation coefficient
for i in range(a):
    # square the difference between the ranks
    d[i] = d[i] ** 2
    # print the squared difference between the ranks
    print(d[i])
    # print the array of squared differences
    print(d)

# finally, calculate the Spearman rank correlation coefficient
print(round(1 - (6 * sum(d)) / (a * (a ** 2 - 1)), 3))


