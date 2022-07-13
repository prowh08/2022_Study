import sys
input=sys.stdin.readline
l=input().strip()
arr=[[0]*26]
arr[0][ord(l[0])-97]=1
for i in range(1,len(l)):
    arr.append(arr[-1][:])
    arr[i][ord(l[i])-97]+=1
for _ in range(int(input())):
    a, s, e=list(input().split())
    s,e=map(int,[s,e])
    sys.stdout.write(str(arr[e][ord(a)-97]-(arr[s-1][ord(a)-97] if s>0 else 0))+"\n")