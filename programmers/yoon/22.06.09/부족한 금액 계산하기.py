def solution(price, money, count):
    answer = -1
    for i in range(1,count+1):
        money-= price*i
    
    if money<0:
        return money*-1
    else:
        return 0

    return answer