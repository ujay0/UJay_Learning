#!/bin/python3

import sys
# Given  names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers.
# You will then be given an unknown number of names to query your phone book for. For each  queried,
# print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for  is not
# found, print Not found instead.


n = int(input())
phoneBook = {}
for i in range(n):
    contact = input().split(' ')
    phoneBook[contact[0]] = contact[1]

print("Give Queries")

# Process Queries
lines = sys.stdin.readlines() # Read all lines from standard input for end press Ctr+D
for i in lines:
    name = i.strip()
    if name in phoneBook:
        print(name + '=' + str( phoneBook[name] ))
    else:
        print('Not found')
