#!/bin/python3

# Task
# There are 3 red marbles and 4 blue marbles in a bag. 
# If 2 marbles are drawn at random without replacement, 
# and the first marble drawn is red, what is the probability 
# that the second marble drawn is blue?

import math
from fractions import Fraction
# Creating two lists of marbles, one with 3 red and 4 blue 
# marbles, and the other with 2 red and 4 blue marbles
lst, lst2 = list('rrrbbbb'), list('rrbbbb')
# Taking the length of both lists to get the total number
#  of marbles in each bag
S1, S2 = len(lst), len(lst2)
# Counting the number of red marbles in the first bag and
A = len([i for i in lst if i == 'r'])
# Counting the number of blue marbles in the second bag
B = len([i for i in lst2 if i == 'b'])

# Calculating the probability of drawing a red marble from
#  the first bag 
prob_A = Fraction(A, S1)
# Calculating the probability of drawing a blue marble from
#  the second bag
prob_B = Fraction(B, S2)

# Calculating the probability of drawing a red marble from
#  the first bag and a blue marble from the second bag
prob_AandB = prob_A * prob_B
# Calculating the conditional probability of drawing a blue marble
#  from the second bag given that a red marble was drawn from
#  the first bag
prob_BgivenA = Fraction ( prob_AandB, prob_A )
# Printing the conditional probability.
print(prob_BgivenA)
