# 검색해봤음

# 람다 함수
# sorted(정렬할 데이터, key 파라미터, reverse 파라미터)

def solution(strings, n):
    return sorted(sorted(strings), key=lambda x: x[n])

strings=["abce", "abcd", "cdx"]
n=2
print(solution(strings, n))