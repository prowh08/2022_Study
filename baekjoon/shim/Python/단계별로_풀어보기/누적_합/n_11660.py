import sys
input=sys.stdin.readline
n,m=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
dp=[[0 for i in range(n+1)]for j in range(n+1)]
for i in range(n):
    for j in range(n):
        dp[i+1][j+1]=dp[i+1][j]+dp[i][j+1]-dp[i][j]+arr[i][j]
for _ in range(m):
    l=list(map(int,input().split()))
    print(dp[l[2]][l[3]]-dp[l[2]][l[1]-1]-dp[l[0]-1][l[3]]+dp[l[0]-1][l[1]-1])