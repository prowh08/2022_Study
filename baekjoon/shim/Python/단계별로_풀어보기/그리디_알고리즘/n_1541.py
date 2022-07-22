l=list(input().split("-"))
s=0
for i in range(len(l)):
    l2=list(map(int,l[i].split("+")))
    if i==0:
        s+=sum(l2)
    else:
        s-=sum(l2)
print(s)