n = int(input())

i = 2
while(i<=n):
    if n%i == 0:
        n = n//i
        print(i)
        i = 2
    else:
        i+=1

