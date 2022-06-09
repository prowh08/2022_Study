import sys

n = int(input())
arr=[]

for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

arr.sort()

for i in range(n):
    print(arr[i][0],arr[i][1],sep=' ',end='\n')