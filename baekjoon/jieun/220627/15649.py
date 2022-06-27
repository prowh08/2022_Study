from itertools import permutations
import sys

n, m = map(int, sys.stdin.readline().split())
l = sorted(permutations(range(1, n+1), m))

for i in l:
    for j in i:
        print(j, end= " ")
    print()