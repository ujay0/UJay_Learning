# A prime is a natural number greater than 1 that has no positive divisors other than 
# 1 and itself. Given a number, N , determine and print whether it is Prime or Not Prime.

# Note: If possible, try to come up with a time complexity algorithm for this problem.



# Enter your code here. Read input from STDIN. Print output to STDOUT

def isPrime(num):
    # Handle edge cases
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:  # Even numbers (except 2) are not prime
        return False
    
    # Check odd divisors only up to √num
    i = 3
    while i * i <= num:  # Equivalent to i <= sqrt(num) but avoids sqrt() call
        if num % i == 0:
            return False
        i += 2  # Only check odd numbers
    
    return True

T = int(input("Enter the Number of Numbers to Check: "))
for _ in range(T):
    N = int(input("Enter the Number to Validated for Prime: "))
    if isPrime(N):
        print("Prime")
    else:
        print("Not Prime")