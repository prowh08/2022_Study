def solution(num):
    selfNumber = list(map(int, range(1, num+1)))
    for i in range(1, num+1):
        n = i
        for j in str(i):
            n += int(j)
        if n in selfNumber:
            selfNumber.remove(n)
    return selfNumber

list = solution(10000)

for num in list:
    print(num)    