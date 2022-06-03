l=list(map(int,input().split()))
print(l[0]//(l[2]-l[1])+1 if l[1]<l[2] else -1)