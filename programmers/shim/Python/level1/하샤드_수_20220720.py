def solution(x):
    s=str(x)
    n=sum(int(s[i]) for i in range(len(s)))
    return (True if x%n==0 else False)