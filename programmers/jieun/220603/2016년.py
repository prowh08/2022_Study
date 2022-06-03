def solution(a, b):
    answer = ''
    day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    if a==1:
        return day[(b+4)%7]
    elif a==2:
        return day[(31+b+4)%7]
    elif a==3:
        return day[(60+b+4)%7]
    elif a==4:
        return day[(91+b+4)%7]
    elif a==5:
        return day[(121+b+4)%7]
    elif a==6:
        return day[(152+b+4)%7]
    elif a==7:
        return day[(182+b+4)%7]
    elif a==8:
        return day[(213+b+4)%7]
    elif a==9:
        return day[(244+b+4)%7]
    elif a==10:
        return day[(274+b+4)%7]
    elif a==11:
        return day[(305+b+4)%7]
    elif a==12:
        return day[(335+b+4)%7]

print(solution(5, 24))