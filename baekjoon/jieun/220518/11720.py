num = int(input())

str = input()
if len(str)!=num:
    str = input()

sum = 0
for i in range(len(str)):
    sum += int(str[i])

print(sum)