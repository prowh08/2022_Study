# 프렉탈 구조

# 다시 검색
# 이해가 안되는데요,,,

def star(n:int, x:list)->list:
    out = []
    if n==3:
        return x
    else:
        for i in x:
            out.append(i*3)
        for i in x:
            out.append(i+' '*len(x)+i)
        for i in x:
            out.append(i*3)
        return star(n//3, out)

n = int(input())
l = ["***", "* *", "***"]
print(star(n,l))
for i in star(n, l):
    print(i)

# 검색해봤는데 이해ㄴ

# def stars(n):
#     arr = []
#     for i in range(3*len(n)):
#         if i//len(n) == 1:
#             arr.append(n[i%len(n)]+" "*len(n)+n[i%len(n)])
#         else:
#             arr.append(n[i%len(n)]*3)
#     return list(arr)

# star = ["***", "* *", "***"]
# n = int(input())
# k = 0
# while n != 3:
#     n = int(n/3)
#     k += 1

# for i in range(k):
#     star = stars(star)
# for i in star:
#     print(i)