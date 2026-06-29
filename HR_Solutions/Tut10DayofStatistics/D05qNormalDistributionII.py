#!/bin/python3

# Task
# The final grades for a Physics exam taken by a large group of students have a mean of u=70 and a 
# standard deviation of o=10. If we can approximate the distribution of these grades by a normal 
# distribution, what percentage of the students:

# Scored higher than 80 (i.e., have a grade > 80 )?
# Passed the test (i.e., have a grade >= 60 )?
# Failed the test (i.e., have a grade < 60 )?
# Find and print the answer to each question on a new line, rounded to a scale of 2 decimal places.

# Input Format
# There are  lines of input (shown below):
# 70 10
# 80
# 60
# The first line contains 2 space-separated values denoting the respective mean and standard deviation 
# for the exam. The second line contains the number associated with question 1. The third line contains
#  the pass/fail threshold number associated with questions 2 and 3.

# Output Format
# There are 3 lines of output. Your answers must be rounded to a scale of 2 decimal places (i.e., 1.23 format):
# On the first line, print the answer to question 1 (i.e., the percentage
# of students who scored higher than 80).
# On the second line, print the answer to question 2 (i.e., the percentage
# of students who passed the test).
# On the third line, print the answer to question 3 (i.e., the percentage
# of students who failed the test).

from math import erf, sqrt

def normal_cdf(x, mean, std_dev):
    """Calculate the cumulative distribution function for a normal distribution."""
    return 0.5 * (1 + erf((x - mean) / (std_dev * sqrt(2))))

# Read input
mean, std_dev = map(float, input().split())
x1 = float(input())
x2 = float(input())

# Calculate probabilities
prob_higher_than_80 = 1 - normal_cdf(x1, mean, std_dev)
prob_passed = 1 - normal_cdf(x2, mean, std_dev)
prob_failed = normal_cdf(x2, mean, std_dev)

# Print results
print(f"{prob_higher_than_80 * 100:.2f}")
print(f"{prob_passed * 100:.2f}")
print(f"{prob_failed * 100:.2f}")