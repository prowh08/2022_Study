def solution(n):
    answer=[]
    st=list(str(n))
    st.reverse()
    for i in st:
        answer.append(int(i))
    return answer