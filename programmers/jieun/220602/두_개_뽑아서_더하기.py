from itertools import combinations

def solution(numbers):
    answer = []
    l = list(combinations(numbers, 2))
    for i in l:
        if i[0]+i[1] not in answer:
            answer.append(i[0]+i[1])
    return sorted(answer)

numbers = [2,1,3,4,1]
print(solution(numbers))