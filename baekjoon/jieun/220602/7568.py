n = int(input())

l = []
for i in range(n):
    w, h = map(int, input().split())
    l.append([w, h])

# rank 더할 생각 어케함 ㅡㅡ;;;
for i in l:
    rank = 1
    for j in l:
        if i[0]<j[0] and i[1]<j[1]:
            rank+=1
    print(rank, end=" ")