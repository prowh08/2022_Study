import sys
from collections import Counter
n,m=map(int,sys.stdin.readline().split())
l=Counter(sys.stdin.readline().split())
l2=Counter(sys.stdin.readline().split())
print(len(l-l2)+len(l2-l))