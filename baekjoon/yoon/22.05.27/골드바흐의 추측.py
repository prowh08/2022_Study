import math
n = int(input())

def sosu(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num%i==0:
            return True
    return False

for i in range(n):
    m = int(input())
    a = m//2
    b = a

    while (sosu(a) or sosu(b)):
        a-=1
        b+=1
    print(a,b)