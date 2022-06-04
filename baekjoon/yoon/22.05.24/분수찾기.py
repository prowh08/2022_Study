n = int(input())

i=0
j=1

while n>i:
    i+=j
    j+=1

a = n - (i-(j-1))

if j%2==0:
    print(str(j-a)+'/'+str(a))
else:
    print(str(a)+'/'+str(j-a))