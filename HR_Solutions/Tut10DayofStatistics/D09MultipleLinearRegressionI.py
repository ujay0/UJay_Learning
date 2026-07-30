#!/bin/python3

# Task
# Andrea has a simple equation
    #  Y = a + b1 * f1 + b2 * f2 + ... + bm * fm

# for (m+1) real constants (a, b1, b2, ..., bm). We can say that the value 
# of Y depends on m features. Andrea studies this equation for n
# different feature sets (f1, f2, ..., fm) and records each respective value of Y.
# If she has q new feature sets, can you help Andrea find the value of Y for each of the sets?
# Input Format
# The first line contains 2 space-separated integers, m (the number of observed features) 
# and n (the number of feature sets Andrea studied), respectively.
# Each of the n subsequent lines contain m+1 space-separated decimals; the first m 
# elements are features (f1, f2, ..., fm), and the last element is the value of Y 
# for the line's feature set.
# The next line contains a single integer, q, denoting the number of feature sets 
# Andrea wants to query for. Each of the q subsequent lines contains m space-separated decimals describing the feature sets.

# Sample Input

# 2 7
# 0.18 0.89 109.85
# 1.0 0.26 155.72
# 0.92 0.11 137.66
# 0.07 0.37 76.17
# 0.85 0.16 139.75
# 0.99 0.41 162.6
# 0.87 0.47 151.77
# 4
# 0.49 0.18
# 0.57 0.83
# 0.56 0.64
# 0.76 0.18


# Output Format
# For each of the q feature sets, print the respective value of Y on a new line
# 105.22
# 142.68
# 132.94
# 129.71

import numpy as np
m, n = map(int, input().strip().split())
c = []
for _ in range(n):
    c.append(list(map(float, input().rstrip().split())))
q = int(input().strip())
e = []
for _ in range(q):
    e.append(list(map(float, input().rstrip().split())))

A = []
for i in range(n):
    A.append(c[i][:-1])
Y = [c[i][-1] for i in range(n)]
a = np.array(A)
Y = np.array(Y)
# Calculate the coefficients using the normal equation
coefficients = np.linalg.inv(a.T @ a) @ a.T @ Y

for row in e:
    # prediction = coefficients[0] + sum(coefficients[i + 1] * row[i] for i in range(len(row))) gives IndexError: index 2 is 
    # out of bounds for axis 0 with size 2
    prediction = coefficients[0] + sum(coefficients[i + 1] * row[i] for i in range(len(row)))
    print(round(prediction, 2))