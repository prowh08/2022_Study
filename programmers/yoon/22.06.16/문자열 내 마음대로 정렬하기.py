import sys

x,y,w,h = map(int,sys.stdin.readline().split())
arr = [x,y,(w-x),(h-y)]
print(min(arr))