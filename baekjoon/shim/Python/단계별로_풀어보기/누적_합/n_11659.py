import sys
input=sys.stdin.readline
n1,n2=map(int,input().split())
l=list(map(int,input().split()))
arr=[0]
for i in range(1,n1+1):
    arr.append(arr[i-1]+l[i-1])
for _ in range(n2):
    o1,o2=map(int,input().split())
    print(arr[o2]-arr[o1-1])