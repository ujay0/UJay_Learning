#!/bin/python3
# Task
# The ratio of boys to girls for babies born in Russia is 1.09 : 1.
# If there is 1 child born per birth, what proportion of Russian 
# families with exactly 6 children will have at least 3 boys?

# Write a program to compute the answer using the above parameters. 
# Then print your result, rounded to a scale of 3 decimal places 
# (i.e., 0.000 format).

from math import factorial

def binomial(n, k):
    # Calculate the binomial coefficient "n choose k"
    return factorial(n) // (factorial(k) * factorial(n - k))

if __name__ == "__main__":
    # Read the ratio of boys to girls
    p , q = map(float, input("Enter the number of boys and girls: ").split())
    # extract the total number of children and calculate the probability of having
    # at least 3 boys in a family of 6 children
    n = 6  # Total number of children
    # Assuming the probability of having a boy is
    # p / (p + q) and the probability of having a girl is q / (p + q)
    total_prob = sum(binomial(n, k) * (p / (p + q)) ** k * (q / (p + q)) ** (n - k) for k in range(3, n + 1))
    # Print the total probability
    print(f"Total probability of having at least 3 boys: {total_prob:.3f}")
