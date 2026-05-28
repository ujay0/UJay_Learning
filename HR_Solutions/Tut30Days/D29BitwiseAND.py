# !/bin/python3

# Given sets S = {1, 2, 3, ..., N} and an integer K, find the maximum value 
# of A & B (where & represents the bitwise AND operator) such that A and B 
# are different members of set S and the value of A & B is less than K.
# 
# 
# Complete the 'bitwiseAnd' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER K




def bitwiseAnd(N, K):
    # Write your code here



if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)

        print(str(res) + '\n')