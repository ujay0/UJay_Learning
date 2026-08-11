#!/bin/python3

# Task
# Suppose a family has 2 children, one of which is a boy. 
# What is the probability that both children are boys?

import math
from fractions import Fraction

# Function to reduce a fraction to its simplest form
def reducto(num, den):
    # Find the greatest common divisor
    pgcd = math.gcd(num, den)
    # Reduce the numerator and denominator by the gcd
    s_num = num // pgcd
    # Reduce the denominator by the gcd
    s_den = den // pgcd
    # Return the reduced numerator and denominator as a tuple
    return s_num, s_den

def prob_direct(nbr_possibilities, favorable_events):
    max_events = nbr_possibilities * nbr_possibilities
    return Fraction(*reducto(favorable_events, max_events))

def prob_comp(frac):
    return 1 - frac

def Bayne(a,b):
    # Calculate the probability of event A given event B using Bayes' theorem
    # P(A|B) = P(A and B) / P(B)
     return a/b

A = prob_direct(2, 1)
B = prob_comp(A) 
C = Bayne(A,B)

print("Bayne:",C)


