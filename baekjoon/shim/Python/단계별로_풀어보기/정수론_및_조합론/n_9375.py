import sys
from collections import Counter
T=int(sys.stdin.readline())
for _ in range(T):
    n=int(sys.stdin.readline())
    l=[]
    for _ in range(n):
        st1,st2=sys.stdin.readline().split()
        l.append(st2)
    c=1
    r=Counter(l)
    for j in r:
        c*=r[j]+1
    print(c-1)