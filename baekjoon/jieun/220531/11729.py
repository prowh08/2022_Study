# 검색했는데 알겠는데 모르겠음

def hanoi(max, start, end, to):
    if max == 1:
        print(start, end)
    else:
        hanoi(max-1, start, to, end)
        print(start, end)
        hanoi(max-1, to, end, start)

n = int(input())
print(2**n-1)
hanoi(n, 1, 3, 2)

