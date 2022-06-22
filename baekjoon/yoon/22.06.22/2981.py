import math
n = int(input())
arr=[]
answer=[]

for _ in range(n):
    arr.append(int(input()))
arr.sort()

an = [arr[i]-arr[i-1] for i in range(1,n)]
gcd = an[0]

for i in range(1,n-1):
    gcd = math.gcd(gcd,an[i])

for i in range(1,int(pow(gcd,1/2))+1):
    if gcd%i==0:
        if i**2 == gcd:
            answer.append(i)
        else:
            answer += [i,gcd//i]
answer.remove(1)
answer.sort()

for i in range(len(answer)):
    print(answer[i],end=' ')