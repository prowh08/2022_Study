def solution(a, b):
    W=['THU','FRI','SAT','SUN','MON','TUE','WED']
    M=[31,29,31,30,31,30,31,31,30,31,30,31]
    return W[(sum(M[i]for i in range(a-1))+b)%7]