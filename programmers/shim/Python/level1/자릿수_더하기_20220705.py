def solution(n):
    answer = 0
    l=list(str(n))
    for i in l:
        answer+=int(i)
    return answer