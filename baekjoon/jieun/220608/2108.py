import sys

n = int(sys.stdin.readline())

l = []
cnt = {}

for i in range(n):
    a = int(sys.stdin.readline())
    l.append(a)
    if a not in cnt.keys():
        cnt[a] =1
    else:
        cnt[a]+=1
l.sort()

most = max(cnt.values())
most_l = []
for key, value in cnt.items():
    if value == most:
        most_l.append(key)
most_l.sort()

print(round(sum(l)/n))
print(l[n//2])
if len(most_l)==1:
    print(most_l[0])
else:
    print(most_l[1])
print(l[n-1]-l[0])