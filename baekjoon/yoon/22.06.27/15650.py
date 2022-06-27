n,m = map(int,input().split())
s=[]

def dfs(t):
    if len(s) == m:
        print(' '.join(map(str,s)))
        return

    for i in range(t,n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()
dfs(1)