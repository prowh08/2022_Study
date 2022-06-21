import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
set_l = sorted(list(set(l)))

# 시간 초과, 검색
# for i in l:
#     for j in range(len(l)):
#         if i == set_l[j]:
#             print(j, end=" ")
#             break

dict = {}
for i in range(len(set_l)):
    dict[set_l[i]] = i
for i in l:
    print(dict[i], end=" ")