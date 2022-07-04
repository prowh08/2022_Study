T=int(input())
if T==1 or T==2:
    print(T)
else:
    arr=[0]*(T+1)
    arr[1]=1
    arr[2]=2
    for i in range(3,T+1):
        arr[i]=(arr[i-1]+arr[i-2])%15746
    print(arr[i])
