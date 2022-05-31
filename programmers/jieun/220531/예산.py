def solution(d, budget):
    answer = 0
    if sum(d) < budget:
        return len(d)
    elif budget == min(d):
        return 1
    else:
        while budget > min(d):
            budget -= min(d)
            d.remove(min(d))
            answer += 1
            if budget == min(d):
                answer += 1
                break
    return answer

# 다른 사람들 풀이보니까 sort해서 앞부터 빼줬으면 되는 것 같군요,,,