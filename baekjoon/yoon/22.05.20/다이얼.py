dial = ['ABC','EDF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
time=0

word = input()

for i in dial:
    for j in i:
        for n in word:
            if n==j:
                time+=dial.index(i)+3

print(time)