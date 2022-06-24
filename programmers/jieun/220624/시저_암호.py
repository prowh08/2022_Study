def solution(s, n):
    temp = ""
    for i in s:
        if 'a'<= chr(ord(i)) <= 'z':
            if chr(ord(i)+n) > 'z':
                temp += chr(ord(i)+n-26)
            else:
                temp += chr(ord(i)+n)
        elif 'A'<= chr(ord(i)) <= 'Z':
            if chr(ord(i)+n) > 'Z':
                temp += chr(ord(i)+n-26)
            else:
                temp += chr(ord(i)+n)
        elif i == " ":
            temp += " "
    return temp

s = "AbC"
n = 4
print(solution(s, n))