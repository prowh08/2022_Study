def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        cut = []
        cut = sorted(array[commands[i][0]-1:commands[i][1]])
        answer.append(cut[commands[i][2]-1:commands[i][2]])
    answer = sum(answer, [])
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))