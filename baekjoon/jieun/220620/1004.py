t = int(input())

l = []
for i in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    cnt = 0
    for j in range(n):
        cx, cy, r = map(int, input().split())
        d1 = ((x1-cx)**2+(y1-cy)**2)**0.5
        d2 = ((x2-cx)**2+(y2-cy)**2)**0.5
        #시작점이나 도착점이 행성 안에 있을 경우
        # 검색함
        if (d1 < r and d2 > r) or (d1 > r and d2 < r):
            cnt += 1
    l.append(cnt)

for c in l:
    print(c)
