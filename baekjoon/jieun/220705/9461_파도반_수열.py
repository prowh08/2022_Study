import sys

# 또 까먹냐 바보야 입니다,,,
p = [0 for i in range(101)]
p[1] = 1
p[2] = 1
p[3] = 1
for i in range(4, 101):
    p[i] = p[i-3]+p[i-2]

n = int(sys.stdin.readline())
for i in range(n):
    m = int(sys.stdin.readline())
    print(p[m])


# 시간초과
# def p(n):
#     if n==1 or n==2 or n==3:
#         return 1
#     else:
#         return p(n-2)+p(n-3)

# n = int(sys.stdin.readline())
# for i in range(n):
#     temp = int(sys.stdin.readline())
#     print(p(temp))
