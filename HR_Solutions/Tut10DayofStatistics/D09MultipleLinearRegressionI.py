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

# from sklearn import linear_model

# # Read feature count (m) and training rows count (n)
# m, n = list(map(int, input().strip().split()))

# X = []
# Y = []
# for i in range(n):
#   inp = list(map(float, input().strip().split()))
#   X.append(inp[:-1])
#   Y.append(inp[-1])

# # Train Linear Regression model
# lm = linear_model.LinearRegression()
# lm.fit(X, Y)

# a = lm.intercept_
# b = lm.coef_

# # Read number of queries
# q = int(input())
# for i in range(q]:
#   f = list(map(float, input().strip().split()))
#   # Calculate predicted Y value
#   res = a + sum([b[j] * f[j] for j in range(m)])
#   print(round(res, 2))

import numpy as np

# Explaination of the code:

# 1. Read the number of features (m) and the number of observations (n)
m, n = [int(i) for i in input().strip().split(' ')]
X = []
Y = []

# 2. Read the feature sets and their corresponding Y values into X and Y lists
for i in range(n):
    data = input().strip().split(' ')
    X.append(data[:m])
    Y.append(data[m:])

# 3. Read the number of new feature sets (q) and store them in X_new
q = int(input().strip())
X_new = []

for x in range(q):
    X_new.append(input().strip().split(' '))

# 4. Convert X, Y, and X_new to numpy arrays for easier mathematical operations
X = np.array(X, float)
Y = np.array(Y, float)
X_new = np.array(X_new, float)

# 5. Center the data by subtracting the mean of each feature from the corresponding
#    feature values in X and the mean of Y from the Y values
X_R = X - np.mean(X, axis=0)
Y_R = Y - np.mean(Y)

# 6. Calculate the beta coefficients using the normal equation for linear regression
beta = np.dot(np.linalg.inv(np.dot(X_R.T, X_R)), np.dot(X_R.T, Y_R))

# 7. Center the new feature sets (X_new) using the mean of the original
#    feature sets (X)
X_new_R = X_new - np.mean(X, axis=0)
Y_new_R = np.dot(X_new_R, beta)
Y_new = Y_new_R + np.mean(Y)

for i in Y_new:
    print(round(float(i.item()), 2))