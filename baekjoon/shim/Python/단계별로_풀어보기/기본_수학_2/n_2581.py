import math
n1=int(input())
n2=int(input())
sum=0
min=0
for i in range(n1, n2+1):
    if i==1: continue
    count=0
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            count+=1
    if(count==0):
        if min==0: min=i
        sum+=i
print(-1 if sum==0 else (f'{sum}\n{min}'))