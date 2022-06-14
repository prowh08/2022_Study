l=input()
count=1
answer=set()
while(count<=len(l)):
    for i in range(0,len(l)-count+1):
        answer.add(l[i:i+count])
    count+=1
print(len(answer))