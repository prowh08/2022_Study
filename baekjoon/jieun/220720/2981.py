# https://yung-developer.tistory.com/51

import sys
 
case = int(input())
num_list = []
for _ in range(case):
    num_list.append(int(sys.stdin.readline().strip()))
 
 
def get_gcd(a, b):  # 유클리드 호제법으로 최대공약수 구하기
    if b > a:
        temp = a
        a = b
        b = temp
    if b == 0:
        return a
    else:
        return get_gcd(b, a % b)
 
 
diffs = []
for i in range(1, len(num_list)):  # 이웃한 숫자의 차이를 구하기
    diffs.append(abs(num_list[i] - num_list[i - 1]))
 
 
gcd = diffs[0]
for i in range(1, len(diffs)):  # 차이들의 최대공약수 구하기
    gcd = get_gcd(diffs[i], gcd)
 
results = []
for i in range(2, int(pow(gcd, 0.5)) + 1):
    if gcd % i == 0:  # 약수 찾기
        results.append(i)
        if gcd // i != i:  # 24 약수를 찾을 때 i가 2라면 12도 추가해야 하므로
            results.append(gcd//i)  # 단 36의 약수 6은 6이 두번 들어가므로 한번만 들어가게
results.append(gcd)  # gcd가 4인 경우 약수로 2와 4가 들어가야하는데 위의 조건에 걸리므로 추가
results.sort()
print(*results)