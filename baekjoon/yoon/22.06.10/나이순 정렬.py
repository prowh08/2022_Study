n = int(input())
arr = []

for _ in range(n):
    age,name = map(str,input().split())
    arr.append((int(age),name))
arr.sort(key=lambda arr:arr[0])

for i in range(n):
    print(arr[i][0],arr[i][1],sep=' ',end='\n')