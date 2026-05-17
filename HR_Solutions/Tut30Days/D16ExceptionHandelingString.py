# Read a string, S, and print its integer value; if S cannot be converted to an integer, 
# print Bad String.

# Note: You must use the String-to-Integer and exception handling constructs built 
# into your submission language. If you attempt to use loops/conditional statements, 
# you will get a  score.

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    S = input().strip()
try:
    print(int(S))
except:
    print('Bad String')
