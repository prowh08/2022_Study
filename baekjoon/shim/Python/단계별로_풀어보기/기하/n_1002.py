# import math
# n=int(input())
# for _ in range(n):
#     l=list(map(int,input().split()))
#     d=math.sqrt((l[0]-l[3])**2+(l[1]-l[4])**2)
#     if d==0 and l[2]==l[5]:
#         print(-1)
#     elif d>l[2]+l[5] or d<abs(l[2]-l[5]):
#         print(0)
#     elif l[2]+l[5]==d or l[2]-l[5]==d or l[5]-l[2]==d:
#         print(1)
#     else:
#         print(2)

#리벤지전

import sys
import math
input=sys.stdin.readline
n=int(input())
for _ in range(n):
    l=list(map(int,input().split()))
    d=math.sqrt((l[0]-l[3])**2+(l[1]-l[4])**2)
    c=1
    if d==0 and l[2]==l[5]:
        c=-1
    elif abs(l[2]-l[5])<d<l[2]+l[5]:
        c=2
    elif abs(l[2]-l[5])>d or l[2]+l[5]<d:
        c=0
    print(c)