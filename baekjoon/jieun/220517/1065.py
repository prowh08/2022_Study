def solution(num):
    count = 0
    for i in range(1, num+1):
        a = []
        for j in str(i):
            a.append(int(j))
        if len(a)<3:
            count+=1
        elif len(a)==3:
            if a[1]-a[0] == a[2]-a[1]:
                count+=1
    return count
                

num = int(input())
print(solution(num))