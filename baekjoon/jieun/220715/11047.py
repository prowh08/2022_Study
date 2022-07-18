# 검색
# https://god-gil.tistory.com/64

n, k = map(int, input().split())

coin = []
for i in range(n):
    coin.append(int(input()))

cnt = 0
for i in range(n-1, -1, -1):
    cnt += k//coin[i] #카운트 값에 K를 동전으로 나눈 몫을 더해줌
    k = k%coin[i] # K는 동전으로 나눈 나머지로 계속 반복

print(cnt)