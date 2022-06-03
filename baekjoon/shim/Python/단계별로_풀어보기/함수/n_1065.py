n=int(input())
result=0
for i in range(100,n+1):
    n_list=list(map(int,str(i)))
    if(n_list[0]-n_list[1]==n_list[1]-n_list[2]):
        result+=1
print(result+ 99 if n>=100 else n)