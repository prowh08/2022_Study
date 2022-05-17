def solution(n):
    han=0
    for i in range(1,n+1):
        if i<100:
            han+=1
        else:
            answer = list(map(int,str(i)))
            if answer[0] - answer[1] == answer[1]-answer[2]:
                han+=1
    return han

n = int(input())
print(solution(n))