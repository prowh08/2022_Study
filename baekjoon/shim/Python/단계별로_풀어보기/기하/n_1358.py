import sys
l=list(map(int,sys.stdin.readline().split()))
c=0
for _ in range(l[4]):
    n,m=map(int,sys.stdin.readline().split())
    if(l[2]<=n<=l[2]+l[0])&(l[3]<=m<=l[3]+l[1]):
        c+=1
        continue
    d1=((n-l[2])**2+(m-(l[3]+l[1]/2))**2)**0.5
    d2=((n-(l[2]+l[0]))**2+(m-(l[3]+l[1]/2))**2)**0.5
    if d1<=l[1]/2 or d2<=l[1]/2:
        c+=1
print(c)