#!/bin/python3
# Task
# A large elevator can transport a maximum of 9800 pounds. Suppose a load of cargo containing 49 boxes must 
# be transported via the elevator. The box weight of this type of cargo follows a distribution with a mean 
# of u=205 pounds and a standard deviation of o=15 pounds. Based on this information, what is the probability 
# that all 49 boxes can be safely loaded into the freight elevator and transported?

# Input Format

# There are 4 lines of input (shown below):
# 9800
# 49
# 205
# 15

# The first line contains the maximum weight the elevator can transport. The second line contains the number of 
# boxes in the cargo. The third line contains the mean weight of a cargo box, and the fourth line contains its 
# standard deviation.

# If you do not wish to read this information from stdin, you can hard-code it into your program.

# Output Format

# Print the probability that the elevator can successfully transport all 49 boxes, rounded to a scale of 4 decimal 
# places (i.e., 1.2345 format).


import math
from scipy.stats import norm

# Read input values
max_weight = float(input())
num_boxes = int(input())
mean_weight = float(input())
std_dev = float(input())

# Calculate the mean and standard deviation of the sum of box weights
sum_mean = num_boxes * mean_weight
sum_std_dev = math.sqrt(num_boxes) * std_dev

# Calculate the probability using the cumulative distribution function (CDF) of the normal distribution
prob = norm.cdf(max_weight, loc=sum_mean, scale=sum_std_dev)

# Print the result rounded to 4 decimal places
print(f"{prob:.4f}")