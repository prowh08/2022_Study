from collections import Counter
n = int(input())
for _ in range(n):
    m = int(input())
    arr=[]
    for _ in range(m):
        a,b = input().split()
        arr.append(b)
    num=1
    answer = Counter(arr)
    for i in answer:
        num*= answer[i]+1
    print(num-1)