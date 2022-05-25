import math
n=int(input())
l=list(map(int,input().split()))
answer=0
for i in range(n):
    count=sum(1 for j in range(2,int(math.sqrt(l[i]))+1) if l[i]%j==0)
    if(l[i]!=1 and count==0): answer+=1
print(answer)