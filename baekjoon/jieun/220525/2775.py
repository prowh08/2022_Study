t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    floor = [i for i in range(1, n+1)]

    for _ in range(k):
        for i in range(1, n):
            floor[i] += floor[i-1]
    print(floor[-1])

# 1층 1 3
# 0층 1 2 3