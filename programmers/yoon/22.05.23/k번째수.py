def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        arr = []
        x = commands[i][0]
        y = commands[i][1]
        z = commands[i][2]
        
        l = sorted(array[x-1:y])
        answer.append(l[z-1])
    return answer