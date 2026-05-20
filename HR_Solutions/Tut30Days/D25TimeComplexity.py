# A prime is a natural number greater than 1 that has no positive divisors other than 
# 1 and itself. Given a number, N , determine and print whether it is Prime or Not Prime.

# Note: If possible, try to come up with a time complexity algorithm for this problem.



# Enter your code here. Read input from STDIN. Print output to STDOUT

def isPrime(num):
    divisers = 0
    i = 1
    while(divisers<3 and i<=num):
        if num%i==0:
            divisers+=1
        i+=1
    if divisers==2:
        return True
    else:
        return False

T = int(input("Enter the Number of Numbers to Check: "))
for _ in range(T):
    N = int(input("Enter the Number to Validated for Prime: "))
    if isPrime(N):
        print("Prime")
    else:
        print("Not Prime")