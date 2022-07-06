import sys

n = int(sys.stdin.readline())
arr=[0]*301
st = [0]*301

for i in range(n):
    arr[i] = int(input())

st[0] = arr[0]
st[1] = arr[1]+arr[0]
st[2] = max(arr[0]+arr[2],arr[1]+arr[2])
for i in range(3,n):
    st[i] = max(st[i-3]+arr[i-1]+arr[i],st[i-2]+arr[i])
print(st[n-1])