#!/bin/python3


# 
# Objective
# Task
# You have a sample of 100 values from a population with mean u=500 and with standard deviation o=80.
# Compute the interval that covers the middle 95% of the distribution of the sample mean; 
# in other words, compute A and B such that P(A < X̄ < B) = 0.95. Use the value of z₀.₀₂₅ = 1.96. 
# Note that X̄ is the sample mean.

# Input Format

# There are five lines of input (shown below):
# 100
# 500
# 80
# .95
# 1.96
# The first line contains the sample size. The second and third lines contain the respective mean (u) 
# and standard deviation (o). The fourth line contains the distribution percentage we want to cover 
# (as a decimal), and the fifth line contains the value of z.


# Output Format
# Print the following two lines of output, rounded to a scale of 2 decimal places (i.e., 1.23  format):

# On the first line, print the value of A.
# On the second line, print the value of B.


print("Enter the sample size:")
n = int(input())
print("Enter the mean:")
u = float(input())
print("Enter the standard deviation:")
o = float(input())
print("Enter the distribution percentage (as a decimal):")
p = float(input())
print("Enter the value of z:")
z = float(input())

critical_value = z
standard_error = o / (n ** 0.5)

A = u - critical_value * standard_error
B = u + critical_value * standard_error

print(f"{A:.2f}")
print(f"{B:.2f}")

