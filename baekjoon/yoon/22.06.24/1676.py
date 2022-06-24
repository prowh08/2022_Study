from math import factorial
n = int(input())
cnt=0
s = str(factorial(n))

for i in s[::-1]:
    if i !='0':
        break
    cnt+=1
print(cnt)