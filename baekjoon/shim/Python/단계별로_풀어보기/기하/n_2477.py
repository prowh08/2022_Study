# import sys
# n = int(sys.stdin.readline())
# l = []
# w = h = w2 = h2 = 0
# for i in range(6):
#     _,m = map(int, sys.stdin.readline().split())
#     l.append(m)
#     if i % 2 == 0:
#         w = max(w, m)
#     else:
#         h = max(h, m)
# for i in range(6):
#     if i % 2 == 0 and h == l[(i+5) % 6]+l[(i+1) % 6]:
#         w2 = l[i]
#     elif i % 2 == 1 and w == l[(i+5) % 6]+l[(i+1) % 6]:
#         h2 = l[i]
# print(n*(w*h - w2*h2))

#리벤지전
import sys
input=sys.stdin.readline
n=int(input())
max_h=max_w=h=w=0
arr=[]
for i in range(6):
    _,m=map(int,input().split())
    arr.append(m)
    if i%2==0:
        max_h=max(max_h,m)
    else:
        max_w=max(max_w, m)
for i in range(6):
    if i%2==0 and max_h==(arr[i%6]+arr[(i+2)%6]):
        h=arr[(i+1)%6]
    elif i%2==1 and max_w==(arr[i%6]+arr[(i+2)%6]):
        w=arr[(i+1)%6]
print((max_h*max_w-w*h)*n)