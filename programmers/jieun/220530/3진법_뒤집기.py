def solution(n):
    if n < 3:
        return n
    else:
        l = []
        while True:
            l.append(n%3)
            n = n//3
            if n<3:
                l.append(n%3)
                break
        l = l[::-1]
        result = 0
        for i in range(len(l)):
            temp = 1
            for j in range(i):
                temp *= 3
            result += l[i]*temp
        return result

n = int(input())
print(solution(n))
