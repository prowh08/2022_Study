n=int(input())
answer=0
for i in range(n,0,-1):
    l=list(map(int,str(i)))
    s=i+sum(l)
    if(s==n):
        answer=i
print(answer)