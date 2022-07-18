import sys
input=sys.stdin.readline
n,m=map(int, input().split())
arr=[]
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
sum=0
for i in arr:
    sum+=m//i
    m%=i
print(sum)