import sys
input=sys.stdin.readline
n=int(input())
a=[]
dp=[0]*(n+1)
for _ in range(n):
    a.append(int(input()))
dp[1]=a[0]
if n>1: dp[2]=dp[1]+a[1]
for i in range(3,n+1):
    dp[i]+=max(dp[i-1],dp[i-2]+a[i-1],dp[i-3]+a[i-2]+a[i-1])
print(dp[n])