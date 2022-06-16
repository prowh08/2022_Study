import sys
n=int(sys.stdin.readline())
arr=[]
for i in range(n):
    n,m=map(int,sys.stdin.readline().split())
    arr.append((n,m))
for i in sorted(arr):
    print(i[0],i[1])