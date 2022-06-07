import sys

n = int(sys.stdin.readline())

l = []
for i in range(n):
    l.append(int(sys.stdin.readline()))
l.sort()

for i in l:
    print(i)
