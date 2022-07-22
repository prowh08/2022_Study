import sys
input=sys.stdin.readline
n=int(input())
s=[]
for _ in range(n):
    num=int(input())
    if num==0:
        s.pop()
    else:
        s.append(num)
print(sum(s))