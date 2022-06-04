a, b, v = map(int, input().split())

k = (v-b)/(a-b)
print(int(k) if k == int(k) else int(k)+1)

# 시간 초과
# i = 0
# while True:
#     i+=1
#     if a + (a-b)*(i-1) >= v or (a-b)*i >= v:
#         print(i)
#         break       