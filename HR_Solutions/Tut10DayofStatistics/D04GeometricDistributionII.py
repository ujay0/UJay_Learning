#!/bin/python3

# Task
# The probability that a machine produces a defective product is 1/3. 
# What is the probability that the 1st defect is found during the first 5th item produced?

# Input Format

# The first line contains the respective space-separated numerator and denominator 
# for the probability of a defect, and the second line contains the inspection we 
# want the probability of the first defect being found during:
#       1 3
#       5

# Output Format

# Print the answer to the question on a new line, rounded to a scale of 3
#  decimal places (i.e., 0.000 format).


from math import pow

if __name__ == "__main__":
    p_numerator, p_denominator = map(int, input("Enter the numerator and denominator for the probability of a defect: ").split())

    inspection_number = int(input("Enter the inspection number for the first defect: "))
    
    p = p_numerator / p_denominator  # Probability of defect
    q = 1 - p  # Probability of non-defect
    
    # Geometric distribution formula: P(X <= k) = 1 - (1 - p)^k
    probability_first_defect_on_or_before_kth_item = 1 - pow(q, inspection_number)

    print(f"Probability that the first defect occurs on the {inspection_number}th item: {probability_first_defect_on_or_before_kth_item:.3f}")
 