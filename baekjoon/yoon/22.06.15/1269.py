import sys
n,m = map(int,input().split())
arr=[]
arr1=[]
answer=[]

arr = set(list(map(int,sys.stdin.readline().split())))
arr1 = set(list(map(int,sys.stdin.readline().split())))

print(len(arr-arr1)+len(arr1-arr))