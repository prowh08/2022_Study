n = int(input())
arr= []
arr = list(map(int,input().split()))
arr.sort()
print(arr[0]*arr[-1])