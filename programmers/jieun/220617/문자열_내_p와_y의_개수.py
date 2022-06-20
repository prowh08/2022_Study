def solution(s):
    cnt_p = 0
    cnt_y = 0
    s = s.lower()
    for i in range(len(s)):
        if s[i]=="p":
            cnt_p+=1
        if s[i]=="y":
            cnt_y+=1
    if cnt_p==cnt_y:
        return True
    else:
        return False