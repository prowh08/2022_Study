n,m=map(int,input().split())
arr=[]
def dfs():
    if len(arr)==m:
        print(' '.join(map(str,arr)))
        return
    for i in range(1,n+1):
        if i not in arr:
            arr.append(i)
            dfs()
            arr.pop()
dfs()


#다른 풀이
# import itertools

# n,m=map(int,input().split())
# num=[i for i in range(1,n+1)]
# arr=itertools.permutations(num,m)
# for i in arr:
#     for j in i:
#         print(j, end=' ')
#     print()