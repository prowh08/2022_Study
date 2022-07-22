import sys
input=sys.stdin.readline
n=int(input())
l=list(map(int,input().split()))
l2=list(map(int,input().split()))
min=l2[0]
sum=l[0]*min
for i in range(1,n-1):
    if min>l2[i]:
        min=l2[i]
    sum+=min*l[i]
print(sum)