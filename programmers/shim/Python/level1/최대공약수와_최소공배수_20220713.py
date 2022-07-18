def gcd(n, m):
    if m==0:
        return n
    else:
        return gcd(m, n%m)
def solution(n, m):
    answer = [gcd(n,m),n//gcd(n,m)*m]
    return answer