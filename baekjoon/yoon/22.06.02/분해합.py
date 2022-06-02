n = int(input())
for i in range(n):
    m = i+sum(list(map(int,str(i))))
    if n == m:
        print(i)
        break
else:
    print(0)