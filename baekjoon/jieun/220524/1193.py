num = int(input())

i = 1
sum = 1

while True:
    sum += i
    i += 1
    if sum > num:
        k = sum - num
        if i%2==0:
            print(str(k)+"/"+str(i-k))
            break
        else:
            print(str(i-k)+"/"+str(k))
            break
