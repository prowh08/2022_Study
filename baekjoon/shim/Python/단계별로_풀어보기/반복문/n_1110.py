n, count=int(input()),0
num=n
while(True):
    num=((num%10)*10+((num//10)+(num%10))%10)
    count+=1
    if(n==num):
        print(count)
        break