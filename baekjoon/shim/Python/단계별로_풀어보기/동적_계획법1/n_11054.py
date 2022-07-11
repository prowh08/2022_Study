import sys
input=sys.stdin.readline
n=int(input())
l=list(map(int,input().split()))
dp=[1]*n
dp2=[0]*n
for i in range(1,n):
    for j in range(i):
        if l[j]<l[i]:
            dp[i]=max(dp[i],dp[j]+1)
for i in range(n-2,-1,-1):
    for j in range(n-1,i,-1):
        if l[j]<l[i]:
            dp2[i]=max(dp2[i],dp2[j]+1)
for i in range(n):
    dp2[i]+=dp[i]
dp2.sort()
print(dp2[n-1])