import sys

n = int(input())
arr=[]

for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

arr.sort(key=lambda arr :(arr[1],arr[0]))

for i in range(n):
    print(arr[i][0],arr[i][1],sep=' ',end='\n')