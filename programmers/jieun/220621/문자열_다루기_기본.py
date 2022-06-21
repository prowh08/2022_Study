def solution(s):
    if len(s)==4 or len(s)==6:
        pass
    else:
        return False
    for i in s:
        if i<'0' or i>'9':
            return False
    return True

s = "12340123"
print(solution(s))