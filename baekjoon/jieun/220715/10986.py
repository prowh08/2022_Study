# 검색

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split())) + [0]
cnt = [0] * m

for i in range(n):
    a[i] += a[i-1]
    cnt[a[i]%m] += 1

ans = cnt[0]

for v in cnt:
    ans += v * (v-1) // 2

print(ans)

# 1. 누적 합(p_sum)을 구한다.
# 2. 누적 합을 m으로 나눈 나머지가 같은 것끼리 분류한다.
# 3. 누적 합의 나머지가 같은 것들 중에서 2개를 조합한다. 
# 이 때 뽑힌 누적합 인덱스를 각각 i와 j라고 하겠다.
# 4. i + 1부터 j까지 구간의 구간합(j번째 누적합 - i번째 누적합)은 m으로 나누어 떨어진다.
# 5. 단, 누적 합의 나머지의 값이 0인 원소들은 혼자만으로도 정답이 된다.

 