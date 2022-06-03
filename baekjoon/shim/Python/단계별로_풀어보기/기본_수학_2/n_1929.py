import math

l=list(map(int, input().split()))
for i in range(l[0],l[1]+1):
    if i==1:
        continue
    b=True
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            b=False
            break
    if b:
        print(i)
