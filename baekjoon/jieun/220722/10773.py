import sys
input = sys.stdin.readline

k = int(input())

l = []
for i in range(k):
    num = int(input())
    if num!= 0:
        l.append(num)
    else:
        l.pop()

print(sum(l))