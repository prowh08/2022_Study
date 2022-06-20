import sys

t = int(sys.stdin.readline())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    d = ((x1-x2)**2+(y1-y2)**2)**0.5
    if d == 0 and r1 == r2: # 같은 중심, 같은 반지름
        print(-1)
    elif abs(r1-r2) == d or r1 + r2 == d: # 내접, 외접
        print(1)
    elif abs(r1-r2) < d < r1 + r2: # 두점에서 만남
        print(2)
    else:
        print(0)