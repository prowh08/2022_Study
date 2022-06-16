import sys
n = int(sys.stdin.readline())
l = []
w = h = w2 = h2 = 0
for i in range(6):
    _,m = map(int, sys.stdin.readline().split())
    l.append(m)
    if i % 2 == 0:
        w = max(w, m)
    else:
        h = max(h, m)
for i in range(6):
    if i % 2 == 0 and h == l[(i+5) % 6]+l[(i+1) % 6]:
        w2 = l[i]
    elif i % 2 == 1 and w == l[(i+5) % 6]+l[(i+1) % 6]:
        h2 = l[i]
print(n*(w*h - w2*h2))
