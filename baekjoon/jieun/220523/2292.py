num = int(input())
room = 1
count = 1

while num > room:
    room = room + (6*count)
    count+=1
print(count)