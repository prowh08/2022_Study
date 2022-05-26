# import math
# def solution(left, right):
#     answer = sum(i for i in range(left, right+1) if pow(int(math.sqrt(i)),2)==i)
#     return sum(i for i in range(left, right+1))-answer*2
# 같은 계산 2번이라 비효율적일듯


import math
def solution(left, right):
    answer=0
    for i in range(left, right+1):
        if pow(int(math.sqrt(i)),2)==i:
            answer-=i
        else: answer+=i
    return answer