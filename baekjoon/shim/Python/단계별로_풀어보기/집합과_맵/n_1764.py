import sys
n,m=map(int,sys.stdin.readline().split())
l1=set()
l2=set()
for _ in range(n):
    l1.add(sys.stdin.readline().strip())
for _ in range(m):
    l2.add(sys.stdin.readline().strip())
l=sorted(list(l1&l2))
print(len(l))
for i in l:
    print(i)