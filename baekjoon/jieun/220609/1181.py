n = int(input())

l = []
for i in range(n):
    word = input()
    l.append(word)
l = list(set(l))
l.sort() # sort하고 다시 sort해야함
l.sort(key = len)

for i in l:
    print(i)