import math
def solution(n):
    answer = 0
    n_sqrt=int(math.sqrt(n))
    answer=(n_sqrt+1)**2 if n_sqrt**2==n else -1
    return answer