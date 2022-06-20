K = int(input())

max_height = 0  # 가장 긴 높이를 저장할 변수
max_width = 0  # 가장 긴 가로길이를 저장할 변수
max_width_index = 0  # 가장 긴 가로길이의 인덱스를 저장할 변수
max_height_index = 0  # 가장 긴 높이의 인덱스를 저장할 변수

info = []  # 변의 정보들을 저장할 리스트

for i in range(6):
    temp = list(map(int, input().split()))
    info.append(temp)
    # 동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4
    if temp[0] == 1 or temp[0] == 2:  # 만약 가로 길이라면
        if max_width < temp[1]:  # 해당 길이가 가장 길다면
            max_width = temp[1]  # 그 길이를 가장긴 가로로 저장한 후
            max_width_index = i  # 그에 해당하는 인덱스를 저장
    else:
        if max_height < temp[1]:  # 해당 길이가 가장 길다면
            max_height = temp[1]  # 그 길이를 가장긴 세로로 저장한 후
            max_height_index = i  # 그에 해당하는 인덱스를 저장

# 그 후 가장 긴 가로 및 세로와 인접한 변 2개와 가장긴 가로와 세로 총 4개를 새로운 리스트에 저장한다.
index_list = [info[max_height_index - 1], info[(max_height_index + 1) % 6], info[max_width_index - 1],
              info[(max_width_index + 1) % 6]]

product = 1  # 곱을 저장할 변수
for i in info:  # 입력받은 변들 중에
    if i not in index_list:  # 만약 새로운 리스트에 저장한 변 4개 중에 없다면 빈 사각형이므로
        product *= i[1]  # 그 넓이를 변수에 저장한다.

result = (max_width * max_height - product) * K  # 전체 큰 직사각형 넓이에서 빈 사각형 넓이를 빼준 후 K를 곱한다.
print(result)