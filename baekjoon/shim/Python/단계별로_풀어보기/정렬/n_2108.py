from collections import Counter
import sys
n=int(sys.stdin.readline())
arr=[]
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort()
max=Counter(arr).most_common()
max_value = 0

if len(max) == 1:
    max_value = max[0][0]
elif max[0][1] == max[1][1]:
    max_value = max[1][0]
else:
    max_value = max[0][0]
print(round(sum(arr)/n),arr[n//2],max_value,arr[n-1]-arr[0], sep="\n")