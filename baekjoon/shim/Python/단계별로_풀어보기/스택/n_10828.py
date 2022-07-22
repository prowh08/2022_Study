import sys
input=sys.stdin.readline
n=int(input())
s=[]
for _ in range(n):
    l=list(input().split())
    if l[0]=="push":
        s.append(int(l[1]))
    elif l[0]=="pop":
        print(-1 if len(s)==0 else s.pop())
    elif l[0]=="size":
        print(len(s))
    elif l[0]=="empty":
        print(1 if len(s)==0 else 0)
    else:
        print(-1 if len(s)==0 else s[-1])