l=list(input())
al=[-1]*26
for i in range(len(l)):
    if al[ord(l[i])-97]==-1:
        al[ord(l[i])-97]=i
for i in al:
    print(i, end=' ')