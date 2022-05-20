n = int(input())
cnt=n

for i in range(n):
    word = input()
    for j in range(len(word)-1):
        if word[j]!= word[j+1]:
            if word[j+1] in word[:j]:
                cnt-=1
                break

print(cnt)