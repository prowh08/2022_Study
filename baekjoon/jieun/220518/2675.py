n = int(input())

a = []

for i in range(n):
    s = input()
    a.append(list(s.split()))

for i in range(n):
    for j in range(0, len(a[i][1])):
        print(int(a[i][0])*a[i][1][j], end="")
    print()

