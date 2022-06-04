arr=[False]*10100
for i in range(1, 10001):
    num=i
    value=i
    while num!=0:
        value+=num%10
        num=num//10
    arr[value]=True
for i in range(1,10001):
    if(arr[i]==False):
        print(i)
