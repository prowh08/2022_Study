n = int(input())
arr=[]
dic={}

arr = list(map(int,input().split()))
num = list(set(arr))
num.sort()

for i in range(len(num)):
    dic[num[i]] = i

for i in arr:
    print(dic[i],end=' ')