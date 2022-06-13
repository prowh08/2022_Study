n = int(input())
arr = set(list(map(int,input().split())))

m = int(input())
arr1 = list(map(int,input().split()))

for i in range(m):
    if arr1[i] in arr:
        print(1,end=' ')
    else:
        print(0,end=' ')
