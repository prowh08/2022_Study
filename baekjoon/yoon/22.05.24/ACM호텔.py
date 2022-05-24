n = int(input())

for i in range(n):
    a,b,c = map(int,input().split())
    
    i = c//a+1
    j = c%a

    if j ==0:
        i-=1
        j=a

    print(j*100+i)