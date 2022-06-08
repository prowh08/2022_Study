def solution(n):
    answer = 0
    for i in range(1,n):
        if n%i==1:
            answer=i
            break
    else:
        answer=3
    return answer