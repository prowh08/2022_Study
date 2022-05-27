import math

while True:
    n = int(input())
    prime = [0,0] + ([1]*(2*n-1))

    if n ==0:
        break

    for i in range(2,int(math.sqrt(2*n+1))+1):
        if prime[i]:
            for j in range(i*2,2*n+1,i):
                prime[j]=0
    answer = [i for i in range(n+1,2*n+1) if prime[i]==1]
    print(len(answer))