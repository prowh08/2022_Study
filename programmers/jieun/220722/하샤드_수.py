def solution(x):
    str_x = str(x)
    h = 0
    for i in str_x:
        h += int(i)
    if x % h == 0:
        return True
    else:
        return False

print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))