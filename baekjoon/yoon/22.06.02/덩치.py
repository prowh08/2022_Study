n = int(input())
arr = []

for _ in range(n):
    a,b = map(int,input().split())
    arr.append((a,b))

for i in arr:
    num=1

    for j in arr:
        if i[0] < j[0] and i[1] < j[1]:
            num+=1

    print(num,end = " ")
"""
n = int(input())
arr = []

for i in range(n):
    a,b = map(int,input().split(' '))
    arr.append((a,b))

for i in range(n):
    num=1

    for j in range(0,n-1):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            num+=1

    print(num,end = " ")
"""