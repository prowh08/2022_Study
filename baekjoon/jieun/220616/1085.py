x, y, w, h = map(int, input().split())

list = [x, y, h-y, w-x]
print(min(list))

