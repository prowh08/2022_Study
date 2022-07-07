import sys
input = sys.stdin.readline

n = int(input())

l = []
for i in range(n):
    l.append(list(map(int, input().split())))

k = 2
for i in range(1, n):
    for j in range(k):
        if j == 0:
            l[i][j] = l[i][j] + l[i - 1][j]
        elif i == j:
            l[i][j] = l[i][j] + l[i - 1][j - 1]
        else:
            l[i][j] = max(l[i - 1][j - 1], l[i - 1][j]) + l[i][j]
    k += 1
print(max(l[n - 1]))
