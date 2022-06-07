def solution(sizes):
    x = 0
    y = 0
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            temp = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = temp
        if x < sizes[i][0]:
            x = sizes[i][0]
        if y < sizes[i][1]:
            y = sizes[i][1]
    return x*y