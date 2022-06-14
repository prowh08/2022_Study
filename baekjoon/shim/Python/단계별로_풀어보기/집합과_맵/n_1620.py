import sys
n,m=map(int,sys.stdin.readline().split())
l={}
for i in range(1,n+1):
    st=sys.stdin.readline().strip()
    l[i]=st
    l[st]=i
for _ in range(m):
    input=sys.stdin.readline().strip()
    if input.isdigit():
        print(l[int(input)])
    else:
        print(l[input])