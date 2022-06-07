def solution(sizes):
    max_w, max_h=0,0
    for i in sizes:
        if(i[0]<i[1]):
            i[0],i[1]=i[1],i[0]
        max_w=max(max_w,i[0])
        max_h=max(max_h,i[1])
    answer = max_w*max_h
    return answer