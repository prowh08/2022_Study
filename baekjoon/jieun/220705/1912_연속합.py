import sys

# 복붙
# https://dojinkimm.github.io/problem_solving/2019/10/21/boj-1912-continuous-sum.html
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
answer = [0] * n
answer[0] = arr[0]
for i in range(1, n):
    answer[i] = max(arr[i], arr[i]+answer[i-1])
print(max(answer))