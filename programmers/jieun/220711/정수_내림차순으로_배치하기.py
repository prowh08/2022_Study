def solution(n):
    l = []
    for i in str(n):
        l.append(i)
    l.sort(reverse=True)
    return int("".join(l))

print(solution(118372))