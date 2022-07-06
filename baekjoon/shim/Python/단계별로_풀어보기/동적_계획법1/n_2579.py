import sys
input=sys.stdin.readline
n=int(input())
l=[]
dp=[0]*(n+1)
for _ in range(n):
    l.append(int(input()))
dp[1]=l[0]
if n>1:
    dp[2]=l[0]+l[1]
for i in range(3,n+1):
    dp[i]=max(dp[i-3]+l[i-2],dp[i-2])+l[i-1]
print(dp[n])