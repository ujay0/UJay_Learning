#!/bin/python3

# Task
# There are 3 red marbles and 4 blue marbles in a bag. 
# If 2 marbles are drawn at random without replacement, 
# and the first marble drawn is red, what is the probability 
# that the second marble drawn is blue?

import math
from fractions import Fraction
lst, lst2 = list('rrrbbbb'), list('rrbbbb')
S1, S2 = len(lst), len(lst2)
A = len([i for i in lst if i == 'r'])
B = len([i for i in lst2 if i == 'b'])

prob_A = Fraction(A, S1)
prob_B = Fraction(B, S2)

prob_AandB = prob_A * prob_B
prob_BgivenA = Fraction ( prob_AandB, prob_A )
print(prob_BgivenA)