l=[(ord(i)-65) for i in list(input())]
for i in range(len(l)):
    if l[i]>17:
        l[i]-=(2 if l[i]==25 else 1)
    l[i]=l[i]//3
print(sum(l)+3*len(l))