from ast import Num


def countnum(n,m):
    cnt = 0
    divnum = m
    while(n >= divnum):
        cnt = cnt+(n // divnum)
        divnum = divnum*m
    return cnt

n,m = map(int,input().split())

print(min(countnum(n,5)-countnum(m,5)-countnum(n-m,5), countnum(n,2)-countnum(m,2)-countnum(n-m,2)))