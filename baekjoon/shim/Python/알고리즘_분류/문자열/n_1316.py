n, cnt=int(input()),0
for i in range(n):
    st=input()
    b=False
    for j in range(len(st)-1):
        if st[j]==st[j+1]:
            continue
        elif st[j] in st[j+1:]:
            b=True
            break
    cnt+=(0 if b==True else 1)
print(cnt)