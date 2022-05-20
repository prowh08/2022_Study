from itertools import combinations

def solution(nums):
    pick3 = list(combinations(nums, 3))
    answer = len(pick3)
    for i in range(len(pick3)):
        sum = pick3[i][0] + pick3[i][1] + pick3[i][2]
        for j in range(2, sum):
            if sum%j == 0:
                answer -= 1
                break 
    return answer
    
nums = [1, 2, 7, 6, 4]
print(solution(nums))
