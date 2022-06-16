arr=[]
arr1 =[]

for _ in range(3):
    x,y = map(int,input().split())
    arr.append(x)
    arr1.append(y)

for i in range(3): 
    if arr.count(arr[i]) == 1: x1 = arr[i]
    if arr1.count(arr1[i])==1: y1 = arr1[i]
print(x1,y1)    

"""
# 코드가 길어
for i in range(3): 
    if arr.count(arr[i]) == 1:
        print(arr[i], end=' ')
for i in range(3): 
    if arr1.count(arr1[i])==1:
        print(arr1[i], end=' ')
"""