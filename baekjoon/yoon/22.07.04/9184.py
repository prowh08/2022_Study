import sys

arr = [[[0 for _ in range(21)] for _ in range (21)] for _ in range (21)]
def w(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20,20,20)
    if arr[a][b][c]:
        return arr[a][b][c]
    if a<b<c:
        arr[a][b][c] = w(a,b,c-1)+w(a,b-1,c-1) - w(a,b-1,c)
    else:
        arr[a][b][c] = w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
    return arr[a][b][c]
    
while(True):
    x,y,z = map(int,sys.stdin.readline().split())
    if x ==-1 and y ==-1 and z == -1:
        break
    else:
        print(f'w({x}, {y}, {z}) = {w(x,y,z)}')