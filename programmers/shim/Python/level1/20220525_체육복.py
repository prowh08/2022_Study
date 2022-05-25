def solution(n, lost, reserve):
    l=[0]*n
    for i in lost:
        l[i-1]-=1
    for i in reserve:
        l[i-1]+=1
    for i in range(len(l)):
        if l[i]==-1:
            if(i!=0 and l[i-1]>0):
                l[i]+=1
                l[i-1]-=1
            elif(i!=len(l)-1 and l[i+1]>0):
                l[i]+=1
                l[i+1]-=1
    answer = sum(1 for i in l if i>=0)
    return answer