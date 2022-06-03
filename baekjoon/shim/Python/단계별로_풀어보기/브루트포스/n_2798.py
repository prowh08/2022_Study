n,m=map(int,input().split())
l=list(map(int,input().split()))
result=0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            s=l[i]+l[j]+l[k]
            if(s<=m and result<s):
                result=s
print(result)

# #다른 풀이
# from itertools import combinations
# n,m=map(int,input().split())
# l=list(map(int,input().split()))
# result=0
# for i in combinations(l,3):
#     s=sum(i)
#     if result<s<=m:
#         result=s
# print(result)
