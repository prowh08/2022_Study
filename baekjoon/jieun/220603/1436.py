n = input()

count = 0
i = 1
while(True):
    if '666' in str(i):
        count+=1
    if count == int(n):
        print(i)
        break
    i+=1
