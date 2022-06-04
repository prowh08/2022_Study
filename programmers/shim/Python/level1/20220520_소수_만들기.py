import math
def solution(nums):
    answer, num = 0,0
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                num=nums[i]+nums[j]+nums[k]
                b=False
                for l in range(2,int(math.sqrt(num))+1):
                    if(num%l==0):
                        b=True
                        break
                answer+=0 if b else 1
    return answer

# 다른 풀이

# from itertools import combinations
# import math
# def is_prime(n):
#     for i in range(2,int(math.sqrt(n))+1):
#         if(n%i==0):
#             return False
#     return True

# def solution(nums):
#     answer = 0
#     cmb=list(combinations(nums,3))
#     for l in cmb:
#         if is_prime(sum(l)):
#             answer+=1
#     return answer

# 파이썬 기본 라이브러리인 itertools의 combinations를 사용하면 리스트에 있는 값들의 조합 쉽게 구하기 가능.
# 리스트에서 모든 순열을 계산=>permutations
# 리스트에서 모든 조합을 계산=>combinations
# 리스트에서 모든 중복 순열을 계산=>product
# 리스트에서 모든 중복 조합을 계산=>combinations_with_replacement
