import sys
T=int(input())
for _ in range(T):
    l=list(map(int,sys.stdin.readline().split()))
    n=int(sys.stdin.readline())
    c=0
    for _ in range(n):
        arr=list(map(int,sys.stdin.readline().split()))
        d1=((l[0]-arr[0])**2+(l[1]-arr[1])**2)**0.5
        d2=((l[2]-arr[0])**2+(l[3]-arr[1])**2)**0.5
        if(arr[2]>d1 and arr[2]>d2):
            pass
        elif arr[2]>d1:
            c+=1
        elif arr[2]>d2:
            c+=1
    print(c)