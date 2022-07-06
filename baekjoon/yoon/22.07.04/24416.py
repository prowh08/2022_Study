def fib(n):
    if n==1 or n==2:
        return 1 # 코드1
    else:
        return (fib(n-1)+fib(n-2))

def fibonacci(n):
    num=0
    f[1],f[2]=-1,-1
    for i in range(3,n+1):
        num+=1
        f[i] = f[i - 1] + f[i - 2];  # 코드2
    return num

f=[i for i in range(0,41)]
n = int(input())

print(fib(n),fibonacci(n))