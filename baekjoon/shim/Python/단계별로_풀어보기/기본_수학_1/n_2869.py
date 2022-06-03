l=list(map(int,input().split()))
print((l[2]-l[1])//(l[0]-l[1])+(0 if (l[2]-l[1])%(l[0]-l[1])==0 else 1))