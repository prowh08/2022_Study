n, m = map(int, input().split())
board = []
cnt = []
for i in range(n):
    board.append(input())
for a in range(n-7):
    for b in range(m-7):
        n1,n2 = 0,0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i + j) % 2 == 0:
                    if board[i][j] != 'W':
                        n1 += 1
                    if board[i][j] != 'B':
                        n2 += 1
                else:
                    if board[i][j] != 'B':
                        n1 += 1
                    if board[i][j] != 'W':
                        n2 += 1                 
        cnt.append(min(n1, n2))
print(min(cnt))