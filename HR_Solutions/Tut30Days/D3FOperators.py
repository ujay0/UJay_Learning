#!/bin/python3
"""
Day
 3: Intro to Conditional Statements
Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as
tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the
meal's total cost. Round the result to the nearest integer.
Example
A tip of 15% * 100 = 15, and the taxes are 8% * 100 = 8. Print the value and return from the
function.
"""

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip_cost = meal_cost * (tip_percent / 100)
    tax_cost = meal_cost * (tax_percent / 100)
    meal_total = meal_cost + tip_cost + tax_cost
    print(round(meal_total))


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
