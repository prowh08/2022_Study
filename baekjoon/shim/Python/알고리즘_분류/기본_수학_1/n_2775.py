T=int(input())
l=[[0]*15 for i in range(15)]
for i in range(15):
    for j in range(15):
        if i==0: l[i][j]=j
        elif j==1: l[i][j]=1
        else: l[i][j]=l[i-1][j]+l[i][j-1]

for i in range(T):
    f=int(input())
    d=int(input())
    print(l[f][d])
