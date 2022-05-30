def solution(n):
    rev=''
    while(n>0):
        a=str(n%3)
        rev+=str(a)
        n=n//3
    return int(rev,3)