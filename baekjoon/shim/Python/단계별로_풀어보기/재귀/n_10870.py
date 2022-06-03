def fibo(n):
    if n>=2:
        n=fibo(n-1)+fibo(n-2)
    return n

n=int(input())
print(fibo(n))