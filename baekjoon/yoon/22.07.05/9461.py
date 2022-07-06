import sys

arr = [0]*101
arr[1] = 1
arr[2] = 1
n = int(sys.stdin.readline())
for _ in range(n):
    m = int(sys.stdin.readline())
    for i in range(3,m+1):
        arr[i] = arr[i-3]+arr[i-2]
    print(arr[m])