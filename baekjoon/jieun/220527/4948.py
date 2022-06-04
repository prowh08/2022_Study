k = 123456*2+1

num_list = [1]*k
for i in range(1, k):
    if i==1:
        continue
    for k in range(2, int(i**0.5)+1):
        if i%k == 0:
            num_list[i] = 0
            break

while True:
    n = int(input())
    sum = 0
    if n == 0:
        break
    for i in range(n+1, 2*n+1):
        sum += num_list[i]
    print(sum)

# import sys

# def isPrime(num):
#     if num == 1:
#         return False
#     else:
#         #에라토스테네스의 체
#         for n in range(2, int(num**0.5)+1):
#             if num%n == 0:
#                 return False
#         return True

# num = -1
# listNum = []
# while(num != 0):
#     num = int(sys.stdin.readline())
#     if num == 0:
#         break
#     listNum.append(num)

# for i in listNum:
#     count = 0
#     for j in range(i, 2*i+1):
#         if isPrime(j):
#             count += 1
#     print(count)