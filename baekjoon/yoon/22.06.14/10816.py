import sys
from collections import Counter
n = int(input())
i = list(map(int,sys.stdin.readline().split()))

m = int(input())
j = list(map(int,sys.stdin.readline().split()))

c = Counter(i)
print(' '.join(f'{c[k]}' if k in c else '0' for k in j))

"""
# 시간초과
n = int(input())
arr = list(map(int,sys.stdin.readline().split()))

m = int(input())
arr1 = list(map(int,sys.stdin.readline().split()))

for i in range(m):
    print(arr.count(arr1[i]),end=' ')
"""
