import math
n = int(input())
arr= []
arr = list(map(int,input().split()))

for i in range(1,n):
    g = math.gcd(arr[0],arr[i])
    print('{0}/{1}'.format(arr[0]//g,arr[i]//g))