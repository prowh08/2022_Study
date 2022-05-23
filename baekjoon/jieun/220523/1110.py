num = int(input())

count = 0

new = -1

while(True):
    if count==0:
        a = num//10
        b = num%10
    else:
        a = new//10
        b = new%10
    new = (a+b)%10 + b*10
    count += 1
    if new == num:
        break

print(count)