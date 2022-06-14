import sys
n,m = map(int,input().split())
arr={}
arr1={}

for i in range(n):
    name = sys.stdin.readline().strip()
    arr[i] = name
    arr1[name] = i

for _ in range(m):
    s = sys.stdin.readline().strip()
    if s.isdigit() == True:
        print(arr[int(s)-1])
    else:
        print(arr1[s]+1)

"""
#시간초과
for _ in range(n):
    i = sys.stdin.readline()
    arr.append(i.lower())

for _ in range(m):
    i = sys.stdin.readline()
    arr1.append(i.lower())

for i in range(m):
    if arr1[i].isdigit():
        print(arr[int(arr1[i])-1])
    if arr1[i] in arr:
        print(arr.index(arr1[i])+1)
"""