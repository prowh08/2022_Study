n,m = map(int,input().split())
arr = list()
board = list()

for _ in range(n):
    arr.append(input())

for i in range(n-7):
    for j in range(m-7):
        w=0
        b=0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if(k+l)%2==0:
                    if arr[k][l]!='W':
                        w+=1
                    if arr[k][l]!='B':
                        b+=1
                else:
                    if arr[k][l]!='B':
                        w+=1
                    if arr[k][l]!='W':
                        b+=1
        board.append(w)
        board.append(b)

print(min(board))