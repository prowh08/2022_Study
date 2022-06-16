import sys
n=int(sys.stdin.readline())
arr=[]
for i in range(n):
    n,m=map(int,sys.stdin.readline().split())
    arr.append((m,n))
for i in sorted(arr):
    print(i[1],i[0])