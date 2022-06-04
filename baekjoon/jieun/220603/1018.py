n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(input())

repair = []
for i in range(n-7):
    for j in range(m-7):
        fw = 0
        fb = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if(k+l)%2 == 0:
                    if board[k][l]!="W":
                        fw = fw+1
                    if board[k][l]!="B":
                        fb = fb+1
                else:
                    if board[k][l]!="B":
                        fw = fw+1
                    if board[k][l]!="W":
                        fw = fw+1
        repair.append(fw)
        repair.append(fb)
print(min(fw, fb))

