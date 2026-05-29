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
def bitwiseAnd_UJ(A, B):
    print("-" * 20)
    print(f"A: {A}, Binary A: {bin(A)}")
    print(f"B: {B}, Binary B: {bin(B)}")
    print(f"A & B: {A & B}")
    for i in range(1, 5):
        print(f"Bit {i}: A bit: {(A >> (i - 1)) & 1}, B bit: {(B >> (i - 1)) & 1}, A & B bit: {((A & B) >> (i - 1)) & 1}")
    print("-" * 20)




# For example, when N = 5 and K = 2, the possible values of A & B are:
#
# 1 & 2 = 0
# 1 & 3 = 1
# 1 & 4 = 0
# 1 & 5 = 1
# 2 & 3 = 2
# 2 & 4 = 0
# 2 & 5 = 0
# 3 & 4 = 0
# 3 & 5 = 1
# 4 & 5 = 4
# The maximum value of A & B that is less than K = 2 is 1.

def bitwiseAnd(N, K):
    max_value = 0
    for A in range(1, N + 1):
        for B in range(A + 1, N + 1):
            current_value = A & B
            if max_value < current_value < K:
                max_value = current_value
            # bitwiseAnd_UJ(A, B)
    return max_value


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)

        print(str(res) + '\n')