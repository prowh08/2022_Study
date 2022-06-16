x=[]
y=[]
for _ in range(3):
    n,m=map(int,input().split())
    x.append(n)
    y.append(m)
for i in range(3):
    if x.count(x[i])==1:
        n=x[i]
    if y.count(y[i])==1:
        m=y[i]
print(n,m)