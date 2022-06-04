def solution(absolutes, signs):
    answer=0
    for absolutes,signs in zip(absolutes,signs):
        if signs:
            answer+=absolutes
        else:
            answer-=absolutes
    return answer