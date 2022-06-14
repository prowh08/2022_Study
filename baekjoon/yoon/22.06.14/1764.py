import sys

n,m = map(int,input().split())
arr = set()
arr1=set()

for _ in range(m):
    arr.add(sys.stdin.readline().strip())
for _ in range(n):
    arr1.add(sys.stdin.readline().strip())

answer = sorted(list(arr1 & arr))

print(len(answer))
for i in answer:
    print(i)

"""
#시간초과
import sys

n,m = map(int,input().split())
arr = []
arr1=[]
answer=[]

for _ in range(m):
    arr.append(sys.stdin.readline().strip())
for i in range(n):
    arr1.append(sys.stdin.readline().strip())
    if arr1[i] in arr:
        answer.append(arr1[i])

print(len(answer))
for i in range(len(answer)):
    print(answer[i],end='\n')
"""