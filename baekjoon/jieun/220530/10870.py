n = int(input())
F = [0, 1]

def fibo(n):
    for i in range(n):
        # F의 마지막 2개 요소를 더해준다.
        F.append(F[-1]+F[-2])
    return F[-2]

print(fibo(n))

#시간 제한

# def fibo(n):
#     if n==0 or n==1:
#         return n
#     else:
#         return fibo(n-1)+fibo(n-2)

# print(fibo(int(input())))