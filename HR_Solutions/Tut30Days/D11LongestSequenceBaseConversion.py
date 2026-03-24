#!/bin/python3

import math
import os
import random
import re
import sys


def toBinary(num):
    binary = []
    while num > 0:
        rem = num % 2
        num = num // 2
        binary.append(rem)
    # print("".join(map(str, binary[::-1])))
    return countOnes(binary)


def countOnes(binary):
    count = 0
    maxseq = 0
    for i in binary:
        if i == 1:
            count += 1
            # print("count: " , count)
            if count > maxseq:
                maxseq = count
                # print("Max: " , maxseq)
        else:
            count = 0
    return maxseq


if __name__ == '__main__':
    n = int(input().strip())
    print(toBinary(n))
