# https://alpyrithm.tistory.com/134

# 최소 비용을 만들기 위해서는 
# 왼쪽에서 오른쪽으로 순차적으로 이동하여 
# 제일 가격이 낮은 주유소에서 기름을 다 넣어야 한다.

import sys
input = sys.stdin.readline

# 도시의 개수, 도로의 길이, 주유소의 리터당 가격
n = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

# 첫 주유는 고정임
res = roads[0]*costs[0]
# 가장 저렴한 주유소
m = costs[0]
# 기름 필요한 도로의 길이 합 
dist = 0

for i in range(1, n-1):
    # 더 저렴한 주유소
    if costs[i] < m:
        res += m*dist
        dist = roads[i]
        m = costs[i]
    else:
        dist += roads[i] 
    
    if i == n-2:
        res += m*dist

print(res)