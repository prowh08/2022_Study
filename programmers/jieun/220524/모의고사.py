def solution(answers):
    answer = []
    num = []
    rule = []
    rule.append([1, 2, 3, 4, 5]*2000)
    rule.append([2, 1, 2, 3, 2, 4, 2, 5,]*1250)
    rule.append([3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*1000)

    for i in rule:
        i = sum([], i)
    
    for i in range(3):
        count = 0
        for j in range(len(answers)):
            if answers[j] == rule[i][j]:
                count+=1
        num.append(count)

    for i in range(3):
        if num[i] == max(num):
            answer.append(i+1)
    
    return answer

answers1 = [1, 2, 3, 4, 5]
answers2 = [1, 3, 2, 4, 2]

print(solution(answers1))
print(solution(answers2))


