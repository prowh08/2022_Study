from math import factorial
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    fac = factorial(m)// (factorial(m-n)*factorial(n))
    print(fac)
