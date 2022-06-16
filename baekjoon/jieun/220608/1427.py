str = input()

l = []
for i in range(len(str)):
    l.append(str[i])
l.sort()
    
l = sorted(l, reverse=True)

print(int(''.join(l)))