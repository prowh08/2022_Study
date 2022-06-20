w,h,x,y,p = map(int,input().split())
ans=0
for _ in range(p):
    x1,y1 = map(int,input().split())

    if (x<=x1<=x+w) and (y<=y1<=y+h):
        ans+=1
        continue
    r = h/2
    d1 = ((x1-x)**2 + (y1-(y+r))**2)**0.5
    d2 = ((x1-(x+w))**2 + (y1-(y+r))**2)**0.5

    if d1<= r or d2 <=r:
        ans+=1

print(ans)
