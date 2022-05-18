n = input().lower()
word = list(set(n))
cnt=0
answer=''

for i in word:
    if cnt < n.count(i):
        answer=i
        cnt = n.count(i)
    elif cnt == n.count(i):
        answer='?'
    
print(answer.upper())