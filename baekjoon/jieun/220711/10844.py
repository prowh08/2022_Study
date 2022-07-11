# https://cotak.tistory.com/12

import sys
input = sys.stdin.readline

n = int(input())

dp = [[0]*10 for _ in range(n+1)]
for i in range(1, 10):
    dp[1][i]=1

mod = 1000000000

for i in range(2, n+1):
    for j in range(10):
        # 0일때는 1만 가능
        if j == 0:
            dp[i][j] = dp[i-1][1]
        # 9일때는 8만 가능
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n])%mod)