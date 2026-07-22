#!/bin/python3

# Task
# A group of five students enrolls in Statistics immediately after taking a Math 
# aptitude test. Each student's Math aptitude test score, x, and Statistics course 
# grade, y, can be expressed as the following list of (x, y) points:
# (95, 85), 
# (85, 95), 
# (80, 70), 
# (70, 65), 
# (60, 70)

# If a student scored an 80 on the Math aptitude test, what grade would we expect 
# them to achieve in Statistics? Determine the equation of the best-fit line 
# using the least squares method, then compute and print the value of x when y=80.

# Input Format

# There are five lines of input; each line contains two space-separated integers
#  describing a student's respective x and y grades:
# 95 85
# 85 95
# 80 70
# 70 65
# 60 70
# Output Format
# Print a single line denoting the answer, rounded to a scale of 3 decimal
#  places (i.e., 1.000 format).

import math
import os
import random
import re
import sys

# a = []
# for _ in range(5):
#     a.append(list(map(int, input().rstrip().split())))

# Read Input from STDIN
# 5
# 95 85
# 85 95
# 80 70
# 70 65
# 60 70
import sys
a = []
for line in sys.stdin:
    a.append(list(map(int, line.split())))
    

a.sort(key=lambda x: x[0])
x = [i[0] for i in a]
y = [i[1] for i in a]

a = sum(x)
b = sum(y)
c = sum([i**2 for i in x])
d = sum([x[i]*y[i] for i in range(len(x))])

n = len(x)
m = (n*d - a*b) / (n*c - a**2)
b = (b - m*a) / n

print(f"{b + m*80:.3f}")
