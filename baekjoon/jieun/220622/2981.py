import sys
import math

n = int(sys.stdin.readline())
l = []
for i in range(n):
    l.append(int(sys.stdin.readline()))


# 이웃한 요소와의 차이 구함
l_diff = []
for i in range(len(l)-1):
    l_diff.append(l[i]-l[i+1])

# 차이들끼리 최대공약수 구함
gcd = l_diff[0]
for i in range(1, len(l_diff)):
    gcd = math.gcd(l_diff[i], gcd)

result = []
for i in range(2, int(pow(gcd, 0.5))+1):
    if gcd%i==0: #약수 찾기
        result.append(i)
        if gcd//i!=i:
            result.append(gcd//i)
result.append(gcd)
result.sort()
print(*result)