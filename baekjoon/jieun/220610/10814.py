import sys

n = int(sys.stdin.readline())
l = []
for i in range(n):
    age, name = sys.stdin.readline().split()
    age = int(age)
    l.append([age, name])
l.sort(key = lambda i:i[0])

for i in l:
    print(i[0], i[1])
