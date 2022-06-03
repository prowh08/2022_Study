l=input().split(" ")
cnt=len(l)
for i in l:
    if i=='':
        cnt-=1
print(cnt)

# 다른 풀이
# print(len(input().split()))

# split()과 split(" ")의 다른점
# split() 공백이 1개이건 여러개이건 1개로 보고 처리한다
# split(" ") 공백을 각각의 공백으로 보고 처리한다.