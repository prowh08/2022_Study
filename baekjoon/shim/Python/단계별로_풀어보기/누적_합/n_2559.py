n,m=map(int,input().split())
l=list(map(int,input().split()))
arr=[0]
ans=[]
for i in range(1,n+1):
    arr.append(arr[i-1]+l[i-1])
    if i>=m:
        ans.append(arr[i]-arr[i-m])
ans.sort()
print(ans[-1])