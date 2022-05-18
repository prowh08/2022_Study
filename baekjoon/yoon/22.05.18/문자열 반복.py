# https://www.acmicpc.net/problem/2675
n = int(input())
alpha=[]

for i in range(n):
    answer=''

    s,m = map(str,input().split(' '))
    for j in range(len(m)):
        answer+=m[j]*int(s)
    alpha.append(answer)

for i in range(n):
    print(alpha[i])