def solution(s):
    answer = ''
    st=s.split(" ")
    for i in range(len(st)):
        for j in range(len(st[i])):
            answer+=st[i][j].upper() if j%2==0 else st[i][j].lower()
        answer+=" "
    return answer[:-1]