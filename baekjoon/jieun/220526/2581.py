a = int(input())
b = int(input())

prime = []
for num in range(a, b+1):
    if num == 1:
        pass
    elif num == 2:
        prime.append(num)
    else:
        for i in range(2, num):
            if num%i == 0:
                break
            elif num%i !=0 and num == i+1:
                prime.append(num)

if len(prime)>=1:
    print(sum(prime))
    print(min(prime))
else:
    print(-1)