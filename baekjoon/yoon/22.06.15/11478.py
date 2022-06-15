n = input()
cnt= set()
for i in range(len(n)):
     for j in range(i,len(n)):
        cnt.add(n[i:j+1])

print(len(cnt))