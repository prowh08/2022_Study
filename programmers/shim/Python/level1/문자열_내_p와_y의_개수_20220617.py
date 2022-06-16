def solution(s):
    s=s.lower()
    answer = True if s.count("p")==s.count("y") else False
    return answer