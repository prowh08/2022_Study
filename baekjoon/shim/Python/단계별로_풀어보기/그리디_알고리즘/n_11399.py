import sys
input=sys.stdin.readline
n=int(input())
l=sorted(list(map(int,input().split())))
sum=0
for i in range(n):
    sum+=(n-i)*l[i]
print(sum)