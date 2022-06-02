T=int(input())
arr=[]
for i in range(T):
    n,m=map(int, input().split())
    arr.append((n,m))
for i in arr:
    r=1
    for j in arr:
        if i==j:
            continue
        if(i[0]<j[0] and i[1]<j[1]):
            r+=1
    print(r, end=" ")