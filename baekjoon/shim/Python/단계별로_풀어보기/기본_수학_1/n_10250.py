n=int(input())
for i in range(n):
    l=list(map(int, input().split()))
    print(l[0]*100+l[2]//l[0] if l[2]%l[0]==0 else l[2]%l[0]*100+l[2]//l[0]+1)
