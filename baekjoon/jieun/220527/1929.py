def isPrime(num):
    if num == 1:
        return False
    else:
        #에라토스테네스의 체
        for n in range(2, int(num**0.5)+1):
            if num%n == 0:
                return False
        return True

a, b = map(int, input().split())
for i in range(a, b+1):
    if isPrime(i):
        print(i)


# 시간 초과

# import math

# a, b = map(int, input().split())

# for i in range(a, b+1):
#     for j in range(2,int(math.sqrt(i))+1):
#         if i%j == 0:
#             break
#         elif i%j != 0 and j == int(math.sqrt(i)):
#             print(i)