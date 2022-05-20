str = input()
count = len(str)

for i in range(len(str)):
    if str[i:i+3]=='dz=':
        count -= 1
    elif str[i:i+2] in ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']:
        count -= 1

print(count)