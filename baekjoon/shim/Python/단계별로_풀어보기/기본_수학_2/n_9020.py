import math

def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    if n==1:
        return False
    return True

T= int(input())
for _ in range(T):
    n = int(input())
    for i in range(n // 2, 0, -1):
        if is_prime(i) & is_prime(n - i):
            print(i, n-i)
            break