import sys 

n = int(sys.stdin.readline())

for i in range(n):
    dict = {}
    cnt = 1
    m = int(sys.stdin.readline())
    for j in range(m):
        cnt = 1
        name, type =  sys.stdin.readline().split()
        if type in dict:
            dict[type] += [name]
        else:
            dict[type] = [name]
    # 수학을 모르는듯;;
    for key in dict.keys():
        cnt *= len(dict[key])+1
    print(cnt-1)
        
