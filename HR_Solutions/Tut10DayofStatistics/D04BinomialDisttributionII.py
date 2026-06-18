#!/bin/python3

# Task
# A manufacturer of metal pistons finds that, on average, 12% of the pistons they manufacture are 
# rejected because they are incorrectly sized. What is the probability that a batch of 10 pistons will contain:

# No more than 2 rejects?
# At least 2 rejects?
# Input Format

# A single line containing the following values (denoting the respective percentage of defective pistons 
# and the size of the current batch of pistons):
# 12 10

# Output Format

# Print the answer to each question on its own line:

# The first line should contain the probability that a batch of 10 pistons will contain no more than 2 rejects.
# The second line should contain the probability that a batch of 10 pistons will contain at least 2 rejects.
# Round both of your answers to a scale of 3 decimal places (i.e., 0.000 format).

from math import factorial

def binomial(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

if __name__ == "__main__":
    p, n = map(float, input("Enter the percentage of defective pistons and the size of the batch: ").split())
    p /= 100  # Convert percentage to probability
    total_prob_no_more_than_2 = sum(binomial(int(n), k) * (p ** k) * ((1 - p) ** (n - k)) for k in range(0, 3))
    total_prob_at_least_2 = 1 - sum(binomial(int(n), k) * (p ** k) * ((1 - p) ** (n - k)) for k in range(0, 2))
    
    print(f"Probability of no more than 2 rejects: {total_prob_no_more_than_2:.3f}")
    print(f"Probability of at least 2 rejects: {total_prob_at_least_2:.3f}")