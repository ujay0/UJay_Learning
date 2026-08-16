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
    # Read the mean of the Poisson distribution and the value for which we want to find the probability
    mean = float(input("Enter the mean of the Poisson distribution: "))
    # Read the value for which we want to find the probability
    x_value = int(input("Enter the value for which you want to find the probability: "))
    
    # Poisson distribution formula: P(X = k) = (λ^k * e^(-λ)) / k!
    # probability = (mean ** x_value) * exp(-mean) / factorial(x_value)
    # In Simpler terms, we can calculate the probability in four steps:
    # Step 1: Calculate λ^k
    lambda_power_k = mean ** x_value
    # Step 2: Calculate e^(-λ)
    e_power_neg_lambda = exp(-mean)
    # Step 3: Calculate k!
    k_factorial = factorial(x_value)
    # Step 4: Calculate the probability
    probability = (lambda_power_k * e_power_neg_lambda) / k_factorial
    
    print(f"Probability that X is equal to {x_value}: {probability:.3f}")