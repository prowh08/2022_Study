import sys

# 검색함, 근데 이해 안되는 
def cnt5(n):
    answer = 0
    while n!=0:
        n = n//5
        answer += n
    return answer

def cnt2(n):
    answer = 0
    while n!=0:
        n = n//2
        answer += n
    return answer

n, m = map(int, sys.stdin.readline().split())

if m == 0:
    print(0)
else:
    print(min(cnt2(n)-cnt2(m)-cnt2(n-m), cnt5(n)-cnt5(m)-cnt5(n-m)))

# 시간 초과
# from math import factorial

# def comb(n, m):
#     return factorial(n)//(factorial(n-m)*factorial(m))

# n, m = map(int, sys.stdin.readline().split())
# c = str(comb(n, m))[::-1]
# cnt = 0
# for i in c:
#     if i == '0':
#         cnt += 1
#     else:
#         break
# print(cnt)