import math

arr=[True for _ in range(2*123456+1)]
arr[0]=False
arr[1]=False

for j in range(2,int(math.sqrt(123456*2))+1):
    if arr[j]:
        i=2
        while(j*i<=2*123456):
            arr[j*i]=False
            i+=1

while(True):
    n=int(input())
    if n==0: break
    count=0
    for i in range(n+1, n*2+1):
        if arr[i]:count+=1
    print(count)