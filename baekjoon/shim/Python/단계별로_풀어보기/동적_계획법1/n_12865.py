import sys
input=sys.stdin.readline
n1,n2=map(int,input().split())
l=[[0,0]]
for _ in range(n1):
    o1,o2=map(int,input().split())
    l.append([o1,o2])
dp=[[0]* (n2+1) for _ in range(n1+1)]
for i in range(1, n1+1):
    for j in range(1,n2+1):
        if(j<l[i][0]):
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-l[i][0]]+l[i][1])
print(dp[n1][n2])