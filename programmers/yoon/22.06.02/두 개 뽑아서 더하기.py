def solution(numbers):
    answer = []
    
    for i in range(0,len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i]+numbers[j])
    return sorted(list(set(answer)))