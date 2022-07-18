# https://suri78.tistory.com/27?category=807697

import sys
input = sys.stdin.readline

n = int(input())

time = list(map(int, input().split()))
time.sort()
for i in range(1, len(time)):
    time[i] += time[i-1]
print(sum(time))

