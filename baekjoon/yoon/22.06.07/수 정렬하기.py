n = int(input())
arr = []

for _ in range(n):
    m = int(input())
    arr.append(m)

arr.sort()

for i in range(n):
    print(arr[i])