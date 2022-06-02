n,m = map(int,input().split())
arr = []
card = 0

arr = list(map(int,input().split(' ')))

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if arr[i]+arr[j]+arr[k] > m:
                continue
            else:
                card = max(card,arr[i]+arr[j]+arr[k])
print(card)
