# 검색함

n = int(input())
count = n

for i in range(n):
    str = input()
    # 이부분 생각못함
    for j in range(len(str)-1):
        if str[j] == str[j+1]:
            pass
        elif str[j] in str[j+1:]:
            count -= 1
            break

print(count)