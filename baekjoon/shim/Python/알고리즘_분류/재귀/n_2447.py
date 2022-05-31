def func(n):
    if n == 3:
        return ['***','* *','***']
    arr = func(n//3)
    r = []
    for i in arr:
        r.append(i*3)
    for i in arr:
        r.append(i+' '*(n//3)+i)
    for i in arr:
        r.append(i*3)
    return r
n=int(input())
print('\n'.join(func(n)))