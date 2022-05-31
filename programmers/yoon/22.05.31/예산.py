def solution(d, budget):
    d.sort()
    answer=0
    for i in range(len(d)):
        if budget-d[i] <0:
            break
        else:
            budget -= d[i]
            answer+=1
    return answer