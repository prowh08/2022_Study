while(True):
    l=sorted(list(map(int,input().split())))
    if l[0]==l[2]==0:
        break
    print("right" if l[0]**2+l[1]**2==l[2]**2 else "wrong")