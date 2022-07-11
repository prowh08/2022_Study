import sys
input=sys.stdin.readline
n=int(input())
l=list(map(int, input().split()))
dp=[1]*n
for i in range(1,n):
    for j in range(0,i):
        if l[j]<l[i]:
            dp[i]=max(dp[j]+1,dp[i])
dp.sort()
print(dp[n-1])