def solution(n):
    answer=""
    l=list(str(n))
    l.sort(reverse=True)
    answer="".join(l)
    return int(answer)