import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x1-x2)**2 + (y1-y2)**2)**0.5
    if d == 0 and r1 == r2: # 원이 같을때
        print(-1)
    elif abs(r1-r2) == d or r1+r2 == d: # 접할때
        print(1)
    elif abs(r1-r2) < d < r1+r2: # 두 점에서 만날때
        print(2)
    else: # 안만날때
        print(0)