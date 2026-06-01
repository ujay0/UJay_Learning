#
# Enter your code here. Read input from STDIN. Print 
# output to STDOUT




import math
from statistics import median
from turtle import mode

def mean(arr):
    return sum(arr)/len(arr)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(mean(arr))