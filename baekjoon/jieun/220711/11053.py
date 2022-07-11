# https://pacific-ocean.tistory.com/153?category=810810

# 예) 수열 l = [10, 20, 10 , 30 , 20, 50]
# 수열	10	20	10	30	20	50
# 길이	1	2	1	3	2	4

import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))

dp = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if l[i] > l[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))