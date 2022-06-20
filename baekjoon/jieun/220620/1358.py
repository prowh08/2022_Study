w, h, x, y, p = map(int, input().split())
cnt = 0
for i in range(p):
    px, py = map(int, input().split())
    #사각형 안
    if x <= px <= x + w and y <= py <= y + h:
        cnt += 1
    #원 안
    elif (px - x) ** 2 + (py - y - h / 2) ** 2 <= (h / 2) ** 2:
        cnt += 1
    elif (px - x - w) ** 2 + (py - y - h / 2) ** 2 <= (h / 2) ** 2:
        cnt += 1
print(cnt)
