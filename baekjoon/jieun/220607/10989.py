# 검색

import sys

n = int(sys.stdin.readline())

l = [0]*10001 # 메모리 효율 위해 미리 만들어둔다.
for i in range(n):
    l[int(sys.stdin.readline())] += 1

for i in range(10001):
    if l[i]!=0:
        for j in range(l[i]):
            print(i) # 인덱스 풀력
