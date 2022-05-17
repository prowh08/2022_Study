n=int(input())
for i in range(n):
    s,l=input().split()
    for j in l:
        print(j*int(s), end="")
    print()