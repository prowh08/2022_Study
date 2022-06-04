n = int(input())
arr = [k for k in map(int,input().split())]
so=0

for i in arr:
    no=0
    if i >1:
        for j in range(2,i):
            if i%j==0:
                no=1
        if no==0:
            so+=1
print(so)