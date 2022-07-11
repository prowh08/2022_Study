def solution(n):
    answer = -1
    for i in range(2, (n//2)+1):
        if n//i == i:
            answer = (i+1)**2
            break
    return answer

print(solution(3))