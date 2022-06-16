def solution(price, money, count):
    i = 1
    while(1):
        cur_price = price*i
        money -= cur_price
        print(money)
        if count==i:
            break
        i+=1
    if money < 0:
        return money*(-1)
    else:
        return 0

price = 3
money = 20
count = 4
print(solution(price, money, count))