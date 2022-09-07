# 복붙
# https://claude-u.tistory.com/371?category=260018

from itertools import permutations
import sys 

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
add, sub, mul, div = map(int, sys.stdin.readline().split())

# 연산자를 숫자로 치환하여 리스트로
operation_list = []
operation_list += [1] * add
operation_list += [2] * sub
operation_list += [3] * mul
operation_list += [4] * div

# 연산자 셋 만들기
operation_set = []
for numbers in list(permutations(operation_list)):
    operation_set.append(numbers)
# 중복 제거
operation_set = list(set(operation_set))

max_answer = -1000000001
min_answer = 1000000001

for case in operation_set:
    answer = a[0] # 첫번째는 앞에 연산자 없으니까~

    for i in range(n-1):
        if case[i] == 1:
            answer += a[i+1]
        elif case[i] == 2:
            answer -= a[i+1]
        elif case[i] == 3:
            answer *= a[i+1]
        elif case[i] == 4:
            if answer < 0:
                answer = -(answer // a[i+1])
            else:
                answer //= a[i+1]
    
    if answer < min_answer:
        min_answer = answer
    if answer > max_answer:
        max_answer = answer    

print(max_answer)
print(min_answer)