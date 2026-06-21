#!/bin/python3

# Task
# A random variable, X, follows Poisson distribution with mean of 2.5. 
# Find the probability with which the random variable X is equal to 5.

# Input Format

# The first line contains X's mean. The second line contains the value
#  we want the probability for:

# 2.5
# 5
# If you do not wish to read this information from stdin, you can 
# hard-code it into your program.

# Output Format

# Print a single line denoting the answer, rounded to a scale of 3 
# decimal places (i.e., 0.000 format).

from math import exp, factorial

if __name__ == "__main__":
    mean = float(input("Enter the mean of the Poisson distribution: "))
    x_value = int(input("Enter the value for which you want to find the probability: "))
    
    # Poisson distribution formula: P(X = k) = (λ^k * e^(-λ)) / k!
    probability = (mean ** x_value) * exp(-mean) / factorial(x_value)
    
    print(f"Probability that X is equal to {x_value}: {probability:.3f}")