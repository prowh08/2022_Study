def solution(sizes):
    for i in range(len(sizes)):
        if sizes[i][0]> sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1],sizes[i][0]
    max0 = max(i[0] for i in sizes)
    max1 = max(i[1] for i in sizes)
    
    return max0*max1