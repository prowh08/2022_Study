def solution(nums):
    answer = len(nums)//2
    if len(set(nums))> answer:
        return answer
    else:
        return len(set(nums))