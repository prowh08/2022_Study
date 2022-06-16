import sys

n = int(sys.stdin.readline())

l = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    l.append([a, b])
l.sort()

for i in l:
    print("%d %d"%(i[0], i[1]))
