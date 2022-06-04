def solution(a, b):
    answer = ''
    week = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    
    answer = (sum(days[:a-1])+b)%7
    
    return week[answer]