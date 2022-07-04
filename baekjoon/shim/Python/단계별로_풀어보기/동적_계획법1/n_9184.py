import sys
arr=[[[0]*21 for _ in range(21)] for _ in range(21)]
def w(x,y,z):
    if(x<=0 or y<=0 or z<=0):
        return 1
    if x>20 or y>20 or z>20:
        return w(20,20,20)
    if arr[x][y][z]:
        return arr[x][y][z]
    if x<y<z:
        arr[x][y][z]=w(x,y,z-1)+w(x,y-1,z-1)-w(x,y-1,z)
        return arr[x][y][z]
    arr[x][y][z]=w(x-1,y,z)+w(x-1,y-1,z)+w(x-1,y,z-1)-w(x-1,y-1,z-1)
    return arr[x][y][z]

while(True):
    l=list(map(int, sys.stdin.readline().split()))
    if l[0]==l[1]==l[2]==-1:
        break
    
    print(f"w({l[0]}, {l[1]}, {l[2]}) = {w(l[0],l[1],l[2])}")

#메모이제이션. 다시 풀어보기