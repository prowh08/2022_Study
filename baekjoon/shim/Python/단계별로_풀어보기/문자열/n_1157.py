st=input().upper()
l=list(set(st))
cnt=[]
for i in l:
    cnt.append(st.count(i))
print("?" if cnt.count(max(cnt))>1 else l[cnt.index(max(cnt))])