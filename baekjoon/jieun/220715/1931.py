# https://suri78.tistory.com/26

import sys

N = int(sys.stdin.readline())
lst = list()
for i in range(N):
    lst.append(list(map(int,sys.stdin.readline().split())))

lst.sort(key=lambda x:(x[1],x[0]))

print(lst)

cnt = 1
last_end_time = lst[0][1]
for i in range(0,N-1):# 시작시간이 처음의 끝시간보다 작으면 안됨
    if last_end_time <= lst[i+1][0]:
        cnt = cnt + 1
        last_end_time = lst[i+1][1]

print(cnt)