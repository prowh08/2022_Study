from itertools import combinations

n, m = map(int, input().split())

num = list(map(int, input().split()))
comb = list(combinations(num, 3))

answer = 0
# m을 넘어서는 x
for i in comb:
    if(m+1>sum(i)):
        answer = max(answer, sum(i))
print(answer)