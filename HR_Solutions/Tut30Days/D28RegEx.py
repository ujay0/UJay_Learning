#!/bin/python3
# Consider a database table, Emails, which has the attributes First Name 
# and Email ID. Given N rows of data simulating the Emails table, print 
# an alphabetically-ordered list of people whose email address ends in '@gmail.com'.


# Input Format

# The first line contains an integer, N, denoting the number of rows in the table.
# Each of the N subsequent lines contains 2 space-separated values: a first 
# name and an email ID.


# Constraints
# 2 <= N <= 30
# Each of the first names consists of lowercase letters only.
# Each of the email IDs consists of lowercase letters, @ and . only.
# The length of the first name not to exceed 20 and email ID not to exceed 50.

# Output Format
# Print an alphabetically-ordered list of first names for every user with a
# gmail.com email address. Each name must be printed on a new line.

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    nameList = []
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]
        
        emailID = first_multiple_input[1]
        if re.search(r'@gmail\.com$', emailID):
            nameList.append(firstName)

    nameList.sort()
    for name in nameList:
        print(name)