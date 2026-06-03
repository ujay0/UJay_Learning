#
# Enter your code here. Read input from STDIN. Print 
# output to STDOUT




import math
from statistics import median
from turtle import mode

def mean(arr):
    return sum(arr)/len(arr)

def mode(arr):
    count = {}
    for i in arr:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    max_count = max(count.values())
    mode = [k for k, v in count.items() if v == max_count]
    return min(mode)

def median(arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 0:
        return (arr[n//2 - 1] + arr[n//2]) / 2
    else:
        return arr[n//2]

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(mean(arr))
    print(median(arr))
    print(mode(arr))