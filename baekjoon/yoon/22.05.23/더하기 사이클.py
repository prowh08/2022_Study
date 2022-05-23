n = int(input())

cnt =0
answer=n

while True:
    if answer<10:
        i = 0
        j = int(answer%10)
    else:
        i = int(answer/10)
        j = int(answer%10)

    answer = (j*10)+(i+j)%10
    cnt+=1
    if answer==n:
        print(cnt)
        break