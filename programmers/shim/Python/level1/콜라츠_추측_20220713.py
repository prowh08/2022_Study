def solution(num):
    n=0
    while(num!=1):
        n+=1
        num=num//2 if num%2==0 else num*3+1
        if n==500:
            break
    return (-1 if n==500 else n)