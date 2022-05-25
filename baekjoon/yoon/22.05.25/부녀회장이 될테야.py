n = int(input())

for i in range(n):
    a = int(input())
    b = int(input())
    
    arr = [k for k in range(1,b+1)]

    for j in range(a):
        for k in range(1,b):
            arr[k] += arr[k-1]
            
    print(arr[-1])