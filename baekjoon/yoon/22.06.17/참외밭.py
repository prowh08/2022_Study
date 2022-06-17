import sys
n = int(sys.stdin.readline())
arr=[]
x = x_idx = y = y_idx=0

for _ in range(6):
    arr.append(list(map(int,sys.stdin.readline().split(' '))))

for i in range(6):
    if arr[i][0]==1 or arr[i][0] == 2:
        if x < arr[i][1]:
            x = arr[i][1]
            x_idx = i
    else:
        if y < arr[i][1]:
            y = arr[i][1]
            y_idx = i

w = abs(arr[(x_idx-1)%6][1] - arr[(x_idx+1)%6][1])
h = abs(arr[(y_idx-1)%6][1] - arr[(y_idx+1)%6][1])
print(((x*y)-(w*h))*n)

"""
# 왜?

x1=[]
y1=[]

for i in range(6):
    if arr[i][0]==1 or arr[i][0] == 2:
        x.append(arr[i][1])
    else:
        y.append(arr[i][1])
answer = max(x)*max(y)- min(x)*min(y)
print(abs(answer)*n)
"""
