import sys

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

for i in range(1,n):
    arr[i] = max(arr[i],arr[i-1]+arr[i])

print(max(arr))