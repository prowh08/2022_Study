n = int(input())

count = 0 
listNum = list(map(int, input().split()))

for num in listNum:
    if num == 1:
        pass
    elif num == 2:
        count += 1
    else:
        for i in range(2, num):
            if num%i == 0:
                break
            elif num%i !=0 and num == i+1:
                count += 1

print(count)