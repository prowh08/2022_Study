import sys
input = sys.stdin.readline

n = int(input())

st = []
for i in range(n):
    str = input().split()
    if str[0] == 'push':
        st.append(str[1])
    elif str[0] == 'pop':
        if len(st) > 0:
            print(st[::-1][0])
            st.pop()
        else:
            print(-1)
    elif str[0] == 'size':
        print(len(st))
    elif str[0] == 'empty':
        if len(st) == 0:
            print(1)
        else:
            print(0)
    elif str[0] == 'top':
        if len(st) == 0:
            print(-1)
        else:
            print(st[::-1][0])