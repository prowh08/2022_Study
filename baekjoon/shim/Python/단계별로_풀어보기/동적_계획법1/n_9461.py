import sys
input=sys.stdin.readline
T=int(input())
arr=[0]*101
arr[0]=arr[1]=arr[2]=1
arr[3]=arr[4]=2
for i in range(5,101):
    arr[i]=arr[i-1]+arr[i-5]
for _ in range(T):
    n=int(input())
    print(arr[n-1])