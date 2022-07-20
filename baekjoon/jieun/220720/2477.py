import sys
input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(6)]

w = 0; w_idx = 0 # 가장 긴 가로 
h = 0; h_idx = 0 # 가장 긴 세로

for i in range(len(arr)):
    if arr[i][0] == 1 or arr[i][0] == 2:
        if w < arr[i][1]:
            w = arr[i][1]
            w_idx = i
    elif arr[i][0] == 3 or arr[i][0] == 4:
        if h < arr[i][1]:
            h = arr[i][1]
            h_idx = i

subW = abs(arr[(w_idx-1)%6][1]-arr[(w_idx+1)%6][1]) # 가장 짧은 가로
subH = abs(arr[(h_idx-1)%6][1]-arr[(h_idx+1)%6][1]) # 가장 짧은 세로

print(((w*h)-(subW*subH))*n)

# l = []
# for i in range(6):
#     l.append(list(map(int, input().split())))

# garo_max = -1
# sero_max = -1
# garo_min = 10000001
# sero_min = 10000001

# for i in range(6):
#     if l[i][0] == 1 or l[i][0] == 2:
#         if garo_max < l[i][1]:
#             garo_max = l[i][1]
#         elif garo_min > l[i][1]:
#             garo_min = l[i][1]
#     elif l[i][0] == 3 or l[i][0] == 4:
#         if sero_max < l[i][1]:
#             sero_max = l[i][1]
#         elif sero_min > l[i][1]:
#             sero_min = l[i][1]

# print(abs((garo_max*sero_max-garo_min*sero_min)*n))