def solution(absolutes, signs):
    result = 0
    for i in range(len(absolutes)):
        if signs[i]==True:
            result += absolutes[i]
        else:
            result -= absolutes[i]
    return result
