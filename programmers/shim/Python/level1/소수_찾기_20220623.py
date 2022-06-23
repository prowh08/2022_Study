import math
def solution(n):
    answer = 0
    arr=[False]*(n+1)
    for i in range(2, int(math.sqrt(n)+1)):
        if arr[i]==True:
            continue
        for j in range(i+i, n+1,i):
            arr[j]=True
    for i in range(2,n+1):
        if(arr[i]==False):
            answer+=1
    return answer