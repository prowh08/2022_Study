# 복붙
# https://hongcoding.tistory.com/118

import sys

graph =  []
blank = []

for i in range(9):
    graph.append(list(map(int, sys.stdin.readline().split())))

# 빈칸 좌표 저장
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i, j)) 

def checkRow(x, a):
    for i in range(9):
        if a == graph[x][i]:
            return False
    return True

def checkCol(y, a):
    for i in range(9):
        if a == graph[i][y]:
            return False
    return True

def checkRect(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == graph[nx+i][ny+j]:
                return False
    return True

def dfs(idx):
    # 전부 다 채웠을때 출력
    if idx == len(blank):
        for i in range(9):
            print(*graph[i])
        exit(0)

    for i in range(1, 10):
        x = blank[idx][0]
        y = blank[idx][1]

        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):
            graph[x][y] = i
            dfs(idx+1)
            # 접답이 없을 경우를 대비해 초기화 시켜놓음
            graph[x][y] = 0

dfs(0)