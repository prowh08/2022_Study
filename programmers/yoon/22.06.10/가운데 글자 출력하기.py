def solution(s):
    if len(s)%2==0:
        m = len(s)//2
        return s[m-1:m+1]
    else:
        return s[len(s)//2]