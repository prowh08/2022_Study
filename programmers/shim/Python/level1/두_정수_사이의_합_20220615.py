def solution(a, b):
    if a>b:
        a,b=b,a
    answer = sum(range(a,b+1))
    return answer