n=int(input())
l=list(map(int,str(n)))
l.sort(reverse=True)
for i in l:
    print(i,end="")