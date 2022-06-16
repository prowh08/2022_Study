def solution(price, money, count):
    answer = sum(i*price for i in range(1,count+1))-money
    answer=0 if answer<=0 else answer
    return answer