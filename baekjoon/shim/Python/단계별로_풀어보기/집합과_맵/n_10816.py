from collections import Counter
import sys

n=int(sys.stdin.readline())
l=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
l2=list(map(int,sys.stdin.readline().split()))
cnt=Counter(l)
for i in l2:
    print(0 if cnt.get(i)==None else cnt.get(i), end=" ")