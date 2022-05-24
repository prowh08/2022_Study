def solution(answers):
    n1=[1,2,3,4,5]
    n2=[2,1,2,3,2,4,2,5]
    n3=[3,3,1,1,2,2,4,4,5,5]
    score=[0,0,0]
    answer = []
    for i in range(len(answers)):
        if(n1[i%5]==answers[i]): 
            score[0]+=1
        if(n2[i%8]==answers[i]): 
            score[1]+=1
        if(n3[i%10]==answers[i]): 
            score[2]+=1
    m=max(score)
    for i in range(3):
        if(score[i]==m): 
            answer.append(i+1)
    return answer