import sys
input=sys.stdin.readline
T=int(input())
dp=[[0]*3 for i in range(T)]
l=list(map(int,input().split()))
for i in range(3):
    dp[0][i]=l[i]
for i in range(1,T):
    l=list(map(int,input().split()))
    dp[i][0]=min(dp[i-1][1],dp[i-1][2])+l[0]
    dp[i][1]=min(dp[i-1][0],dp[i-1][2])+l[1]
    dp[i][2]=min(dp[i-1][0],dp[i-1][1])+l[2]
print(min(dp[T-1][0],dp[T-1][1],dp[T-1][2]))