import sys
input=sys.stdin.readline
T=int(input())
dp=[]
for i in range(T):
    dp.append(list(map(int,input().split())))
for i in range(T-1,-1,-1):
    for j in range(i):
        dp[i-1][j]+=max(dp[i][j],dp[i][j+1])
print(dp[0][0])