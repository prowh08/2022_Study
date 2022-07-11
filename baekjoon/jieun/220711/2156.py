# https://pacific-ocean.tistory.com/152

n = int(input())

w = [0]
for i in range(n):
    w.append(int(input()))

dp = [0]
dp.append(w[1])

if n > 1:
    dp.append(w[1] + w[2])

for i in range(3, n + 1):
    dp.append(max(dp[i - 1], dp[i - 3] + w[i - 1] + w[i], dp[i - 2] + w[i]))

print(dp[n])


# 메모리 초과 ㅡㅡ
# from itertools import combinations

# import sys
# input = sys.stdin.readline

# n = int(input())

# l = []
# for _ in range(n):
#     l.append(int(input()))

# max = -1
# for i in list(combinations(range(n), 3)):
#     if i[2]-i[1] == 1 and i[1]-i[0] == 1:
#         pass
#     else:
#         if max < l[i[2]]+l[i[1]]+l[i[0]]:
#             max = l[i[2]]+l[i[1]]+l[i[0]]

# print(max)