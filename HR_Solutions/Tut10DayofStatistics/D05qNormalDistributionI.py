#!/bin/python3

# Task
# In a certain plant, the time taken to assemble a car is a random variable, X, having a normal distribution with a mean of 20 hours and a standard deviation 
# of 2 hours. What is the probability that a car can be assembled at this plant in:

# Less than 19.5 hours?
# Between 20 and 22 hours?

# Input Format
# There are 3 lines of input (shown below):

# 20 2
# 19.5
# 20 22

# The first line contains 2 space-separated values denoting the respective mean and standard deviation for X. The second line contains the number associated
#  with question 1. The third line contains  space-separated values describing the respective lower and upper range boundaries for question 2.

# Output Format

# There are two lines of output. Your answers must be rounded to a scale of 3 decimal places (i.e., 1.234 format):

# On the first line, print the answer to question 1 (i.e., the probability that a car can be assembled in less than 19.5 hours).
# On the second line, print the answer to question 2 (i.e., the probability that a car can be assembled in between 20 and 22 hours).

from math import erf, sqrt

def normal_cdf(x, mean, std_dev):
    """Calculate the cumulative distribution function for a normal distribution."""
    return 0.5 * (1 + erf((x - mean) / (std_dev * sqrt(2))))

# Read input
mean, std_dev = map(float, input().split())
x1 = float(input())
x2_lower, x2_upper = map(float, input().split())

# Calculate probabilities
prob1 = normal_cdf(x1, mean, std_dev)
prob2 = normal_cdf(x2_upper, mean, std_dev) - normal_cdf(x2_lower, mean, std_dev)

# Print results
print(f"{prob1:.3f}")
print(f"{prob2:.3f}")