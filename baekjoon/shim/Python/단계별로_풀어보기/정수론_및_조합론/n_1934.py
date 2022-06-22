import sys
from math import gcd
# def func(n,m):
#     if m==0:
#         return n
#     else:
#         return func(m,n%m)
# T=int(input())
# for _ in range(T):
#     n,m=map(int,sys.stdin.readline().split())
#     f=func(n,m)
#     print(n//f*m)

T=int(input())
for _ in range(T):
    n,m=map(int,sys.stdin.readline().split())
    f=gcd(n,m)
    print(n//f*m)