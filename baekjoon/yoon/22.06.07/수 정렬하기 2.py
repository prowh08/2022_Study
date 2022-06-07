import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    m = int(sys.stdin.readline())
    arr.append(m)

arr.sort()

for i in range(n):
    print(arr[i])