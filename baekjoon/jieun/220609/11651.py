import sys

n = int(sys.stdin.readline())

l = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    l.append([b,a])
l.sort()

for i in range(n):
    l[i] = l[i][::-1]

for i in l:
    print("%d %d"%(i[0], i[1]))