import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    lcnt = 0; rcnt = 0
    str = input()
    for i in str:
        if i == '(': 
            lcnt += 1
        elif i == ')': 
            rcnt += 1
        if lcnt < rcnt:
            break
    if lcnt == rcnt:
        print("YES")
    else:
        print("NO")