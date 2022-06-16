def solution(strings, n):
    answer = []
    for i in strings:
        answer.append(i[n]+i)
    answer.sort()
    for i in range(len(answer)):
        answer[i]=answer[i][1:]
    return answer