n = int(input())
m = int(input())
arr=[]

for i in range(n,m+1):
    no=0
    if i>1:
        for j in range(2,i):
            if i%j==0:
                no=1
                break
        if no==0:
            arr.append(i)

if len(arr)>0:
    print(sum(arr))
    print(arr[0])
else:
    print(-1)