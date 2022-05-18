#검색해봤습니다,,,

word = input()
alphabet = list(range(97, 123))

for x in alphabet:
    print(word.find(chr(x)), end=" ")