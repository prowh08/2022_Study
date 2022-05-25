def solution(n, lost, reserve):

    reserve_n = list(set(reserve) - set(lost))
    lost_n = list(set(lost) - set(reserve))

    answer = n - len(lost_n)

    for i in lost_n:

        if i-1 in reserve_n:
            answer += 1
            reserve_n.remove(i-1)

        elif i+1 in reserve_n:
            answer += 1
            reserve_n.remove(i+1)

    return answer

# def solution(n, lost, reserve):

#     answer1 = n - len(lost)
#     answer2 = n - len(lost)

#     for i in lost:
        
#         if i-1 in reserve:
#             reserve.remove(i-1)
#             answer1 += 1

#         elif i+1 in reserve:
#             reserve.remove(i+1)
#             answer1 += 1

#     for i in lost:
        
#         if i+1 in reserve:
#             reserve.remove(i+1)
#             answer2 += 1

#         elif i-1 in reserve:
#             reserve.remove(i-1)
#             answer2 += 1

#     return max(answer1, answer2)