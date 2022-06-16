lx = []
ly = []

for i in range(3):
    x, y = map(int, input().split())
    lx.append(x)
    ly.append(y)

# count 
for i in range(3):
    if lx.count(lx[i])==1:
        ax = lx[i]
    if ly.count(ly[i])==1:
        ay = ly[i]

print(ax, ay)




