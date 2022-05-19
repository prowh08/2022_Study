# dictionary, list comprehend 이용

word = input().upper()

alphaCount = {}

for a in word:
    if a not in alphaCount:
        alphaCount[a] = 1
    else:
        alphaCount[a] += 1

max_key = [k for k, v in alphaCount.items() if max(alphaCount.values())==v]

if len(max_key)==1:
    print(max_key[0])
else:
    print("?")


