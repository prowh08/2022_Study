import sys
from math import factorial

def comb(n, k):
    return factorial(n)//(factorial(n-k)*factorial(k))

n = int(sys.stdin.readline())
for i in range(n):
    n, m = map(int, sys.stdin.readline().split())
    print(comb(m, n))
