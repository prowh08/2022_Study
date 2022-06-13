n=int(input())
l=list(map(int, input().split()))
l.sort()
m=int(input())
l2=list(map(int,input().split()))
for i in l2:
    max,min,middle=n-1,0,0
    b=False
    while max>=min:
        middle=(max+min)//2
        if l[middle]>i:
            max=middle-1
        elif l[middle]<i:
            min=middle+1
        else:
            print(1,end=" ")
            b=True
            break
    if b==False:
        print(0,end=" ")