n,m = map(int,input().split())
arr=[]
arr1=[]
cnt=0

for _ in range(n):
    a = input()
    arr.append(a)

for _ in range(m):
    a = input()
    arr1.append(a)

for i in range(m):
    if arr1[i] in arr:
        cnt+=1
print(cnt)