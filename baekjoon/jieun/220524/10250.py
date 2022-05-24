t = int(input())

result = []
for i in range(t):
    h, w, n=map(int, input().split())
    floor = n%h
    room = n//h + 1
    # floor = 0 인 경우 생각못함
    if floor == 0: 
        room -= 1
        floor = h
    num = floor*100 + room 
    result.append(num)

for i in result:
    print(i)
    

    