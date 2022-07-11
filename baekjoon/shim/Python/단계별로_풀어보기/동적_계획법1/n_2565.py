import sys
input=sys.stdin.readline
n=int(input())
l=[]
dp=[1]*n
for _ in range(n):
    n1,n2=map(int, input().split())
    l.append([n1,n2])
l.sort()
for i in range(1,n):
    for j in range(i):
        if l[j][1]<l[i][1]:
            dp[i]=max(dp[i],dp[j]+1)
dp.sort()
print(n-dp[n-1])