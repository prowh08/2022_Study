def hanoi(n, f, b, t):
    if(n==1):
        print(f, t)
    else:
        hanoi(n-1,f, t, b)
        print(f,t)
        hanoi(n-1,b,f,t)
n=int(input())
print(2**n-1)
hanoi(n,1,2,3)