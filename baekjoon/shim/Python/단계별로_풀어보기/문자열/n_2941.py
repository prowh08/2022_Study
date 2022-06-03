l=['c=','c-','dz=','d-','lj','nj','s=','z=']
st=input()
for i in l:
    st=st.replace(i,'.')
print(len(st))