word = ['c=','c-','dz=','d-','lj','nj','s=','z=']

s = input()

for i in word:
    s = s.replace(i,'*')

print(len(s))