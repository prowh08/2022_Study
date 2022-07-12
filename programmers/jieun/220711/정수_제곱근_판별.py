def solution(n):
    answer = -1
    if n == 1:
        answer = 4
    elif n > 1:
        for i in range(2, n//2+1):
            if n/i == i:
                answer = (i+1)*(i+1)
                break
    return answer

print(solution(5))