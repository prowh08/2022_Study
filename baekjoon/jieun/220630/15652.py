from itertools import combinations_with_replacement
import sys

n, m = map(int, sys.stdin.readline().split())
l = combinations_with_replacement(range(1, n+1), m)

for i in l:
    for j in i:
        print(j, end=" ")
    print()