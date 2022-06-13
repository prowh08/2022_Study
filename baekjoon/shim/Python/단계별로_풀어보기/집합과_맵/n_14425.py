import sys
n,m=map(int,sys.stdin.readline().split())
list=[]
for _ in range(n):
    list.append(sys.stdin.readline())
count=0
for _ in range(m):
    if sys.stdin.readline() in list:
        count+=1
print(count)