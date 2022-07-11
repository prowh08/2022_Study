
import sys
input = sys.stdin.readline

n = input()

l = []

for _ in range(n):
    l.append(list(map(int, input().split())))

# 첫번째 전봇대를 기준으로 오름차순 정렬 후
# 첫번째 전봇대와 연결되어 있는 두번째 전봇대의 수를 LIS (최장 증가 수열)로 구해주면
# 연결될 수 있는 최대 전깃줄의 수가 나옵니다.

l.sort()

dp = [1]*n
for i in range(n):
    for j in range(i):
        if l[i][1] > l[j][1] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

# 없애야 하는 전깃줄의 최소 개수 = 현재 전깃줄의 개수 - 겹치지 않는 최대 전깃줄의 개수
print(n-max(dp))