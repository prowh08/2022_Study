import sys, statistics
from collections import Counter
n = int(input())
arr=[]

for _ in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort()

print(round(sum(arr)/n))
#print(arr[len(arr)//2])
print(statistics.median(arr))

#print(statistics.mode(arr)) # 첫번째 값만 출력되므로 안됨

mode = Counter(arr).most_common()

if len(arr) > 1 : 
    if mode[0][1] == mode[1][1]:
        print(mode[1][0])
    else : 
        print(mode[0][0])
else : 
    print(mode[0][0])

print(max(arr)-min(arr))