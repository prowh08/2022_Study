n = int(input())
for _ in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    m = int(input())
    ans=0

    for _ in range(m):
        x,y,z = map(int,input().split())
        dis1 = (((x1-x)**2) + ((y1-y)**2))**0.5
        dis2 = (((x2-x)**2) + ((y2-y)**2))**0.5
        
        if(dis1<z and dis2>z) or (dis1>z and dis2<z):
            ans+=1

    print(ans)