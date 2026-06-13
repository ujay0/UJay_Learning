#!/bin/python3

# Task
# Suppose a family has 2 children, one of which is a boy. 
# What is the probability that both children are boys?

import math
from fractions import Fraction

def reducto(num, den):
    pgcd = math.gcd(num, den)
    s_num = num // pgcd
    s_den = den // pgcd
    return s_num, s_den

def prob_direct(nbr_possibilities, favorable_events):
    max_events = nbr_possibilities * nbr_possibilities
    return Fraction(*reducto(favorable_events, max_events))

def prob_comp(frac):
    return 1 - frac

def Bayne(a,b):
     return a/b

A = prob_direct(2, 1)
B = prob_comp(A) 
C = Bayne(A,B)

print("Bayne:",C)


