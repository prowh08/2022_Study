from itertools import combinations
n,m = map(int, input().split())

combi = list(combinations(range(n),m))
print(len(combi))