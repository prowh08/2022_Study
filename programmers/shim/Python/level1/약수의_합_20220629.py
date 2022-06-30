import math
def solution(n):
    answer = 0
    for i in range(1,int(math.sqrt(n+1))+1):
        if(n%i==0 and n!=0):
            answer+=i+((n//i)if n//i!=i else 0)
    return answer