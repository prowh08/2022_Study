def solution(s):
    m = list(s)
    m.sort(reverse=True)
    return ''.join(m)