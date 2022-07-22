import sys
input=sys.stdin.readline
n=int(input())
for _ in range(n):
    l=list(input().strip())
    s=[]
    b=False
    for i in l:
        if i=='(':
            s.append('(')
        else:
            if len(s)==0:
                b=True
                break
            else:
                s.pop()
    if b or len(s)!=0:
        print("NO")
    else:
        print("YES")