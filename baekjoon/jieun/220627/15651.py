from itertools import product
import sys

n, m = map(int, sys.stdin.readline().split())

for i in product(range(1, n+1), repeat=m):
    for j in i:
        print(j, end=" ")
    print()
