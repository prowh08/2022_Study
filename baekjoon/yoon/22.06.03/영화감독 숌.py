n = int(input())
m = 666
cnt=0

while True:
    if '666' in str(m):
        cnt+=1
        if cnt == n:
            print(m)
            break
    m+=1