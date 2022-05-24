def solution(answers):
    answer = []
    cnt=0
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a1,c1,b1=0,0,0
    
    for i in range(0,len(answers)):
        if answers[i] == a[i%5]:
            a1+=1
        if answers[i] == b[i%8]:
            b1+=1
        if answers[i] == c[i%10]:
            c1+=1
    n = max(a1,b1,c1)
    
    if n == a1:
        answer.append(1)
    if n == b1:
        answer.append(2)
    if n == c1:
        answer.append(3)
        
    return answer