n=int(input())-1
count=0
while(n>0):
    count+=1
    n-=count*6
print(count+1)