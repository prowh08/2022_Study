def solution(a, b):
    answer = 0
    if len(a)==len(b):
        for i in range(len(a)):
            answer += a[i]*b[i]
    return answer