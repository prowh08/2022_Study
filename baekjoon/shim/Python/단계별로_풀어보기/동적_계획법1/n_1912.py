import sys
input=sys.stdin.readline
n=int(input())
sum=0
l=list(map(int,input().split()))
maxi=l[0]
for i in range(n):
    sum+=l[i]
    maxi=max(sum,maxi)
    if(sum<0):
        sum=0
print(maxi)