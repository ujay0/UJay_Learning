#!/bin/python3
# Task

# The manager of a industrial plant is planning to buy a machine of 
# either type A or type B. For each day’s operation:

# The number of repairs, X, that machine A needs is a Poisson random
#  variable with mean 0.88. The daily cost of operating machine A is
#  160 + 40 * X^2.
# The number of repairs, Y, that machine B needs is a Poisson random
#  variable with mean 1.55. The daily cost of operating machine B is
#  128 + 40 * Y^2.
# Assume that the repairs take a negligible amount of time and the
#  machines are maintained nightly to ensure that they operate like
#  new at the start of each day. Find and print the expected daily
#  cost for each machine.
# Input Format

# A single line comprised of 2 space-separated values denoting the
#  respective means for  and :

# 0.88 1.55

# There are two lines of output. Your answers must be rounded to a scale of  decimal places (i.e.,  format):

# On the first line, print the expected daily cost of machine A.
# On the second line, print the expected daily cost of machine B.

from math import exp, factorial

def poisson_pmf(k, lam):
    return (lam ** k) * exp(-lam) / factorial(k)

def expected_cost(lam, cost_function):
    total_cost = 0
    for k in range(20):  # Assuming a reasonable upper limit
        prob = poisson_pmf(k, lam)
        total_cost += prob * cost_function(k)
    return total_cost

# Read input
mean_A, mean_B = map(float, input().split())

# Define cost functions
cost_A = lambda x: 160 + 40 * x ** 2
cost_B = lambda y: 128 + 40 * y ** 2

# Calculate expected costs
expected_cost_A = expected_cost(mean_A, cost_A)
expected_cost_B = expected_cost(mean_B, cost_B)

# Print results
print(f"{expected_cost_A:.3f}")
print(f"{expected_cost_B:.3f}")