def solution(nums):
    l=set(nums)
    answer = min(len(l),len(nums)//2)
    return answer