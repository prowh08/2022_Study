import math

def isPrime(x):
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

def solution(n):
    cnt = 0
    for i in range(2, n+1):
        if isPrime(i):
            cnt += 1
    return cnt 

n = 10
print(solution(n))