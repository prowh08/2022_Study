# 검색

def solution(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    return [c, int(a*b/c)]

# 유클리드 호제법: 최대공약수를 구하는 알고리즘
# a와 b에 대해서(a<b) r=a%b이라고 하면, 
# r==0이 될 때까지 b%r=r', r%r'을 했을 때 r'이 최대공약수이다.
# 최소공배수: (a*b)/최대공약수

print(solution(3, 12))