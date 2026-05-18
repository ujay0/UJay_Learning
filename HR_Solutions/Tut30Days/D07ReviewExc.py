# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
for i in range(0,N):
    userString = input()
    evenStr=[]
    oddStr=[]
    for j in range(0,len(userString)):
        if j % 2 == 0:
            evenStr.append(userString[j])
        elif j % 2 != 0:
            oddStr.append(userString[j])
    print("".join(evenStr), end=' ')
    print("".join(oddStr))