from os import sep
import sys
arr=[]
n = int(sys.stdin.readline())

for i in str(n):
    arr.append(int(i))
arr.sort(reverse=True)

for i in arr:
    print(i,end='')
