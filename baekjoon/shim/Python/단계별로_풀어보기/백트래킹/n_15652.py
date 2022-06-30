n,m=map(int,input().split())
arr=[]
def dfs(s):
    if len(arr)==m:
        print(' '.join(map(str,arr)))
        return
    for i in range(s,1+n):
        arr.append(i)
        dfs(i)
        arr.pop()

dfs(1)