def solution(n):
    l = []
    for i in str(n):
        l.append(int(i))
    return l[::-1]

print(solution(12345))