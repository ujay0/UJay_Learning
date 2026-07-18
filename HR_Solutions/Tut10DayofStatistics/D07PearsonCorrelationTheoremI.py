# !/bin/python3

# Task
# Given two n-element data sets, X and Y, calculate the value of the Pearson correlation coefficient.

# Input Format

# The first line contains an integer, n, denoting the size of data sets X and Y.
# The second line contains n space-separated real numbers (scaled to at most one decimal place), defining data set X.
# The third line contains n space-separated real numbers (scaled to at most one decimal place), defining data set Y.

# Constraints

# 10 <= n <= 100
#  1 < Xi < 100, where Xi is the ith value of data set X.
#  1 < Yi < 100, where Yi is the ith value of data set Y.
# Data set X contains unique values.
# Data set Y contains unique values.
# Output Format

# Print the value of the Pearson correlation coefficient, rounded to a scale of 3 decimal places.

n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))

a = sum(x) / n
b = sum(y) / n
k = sum([(x[i] - a) * (y[i] - b) for i in range(n)])
l = (sum([(x[i] - a) ** 2 for i in range(n)]) ** 0.5) * (sum([(y[i] - b) ** 2 for i in range(n)]) ** 0.5)
print(round(k / l, 3))

from scipy.stats import pearsonr
print(round(pearsonr(x, y)[0], 3))
