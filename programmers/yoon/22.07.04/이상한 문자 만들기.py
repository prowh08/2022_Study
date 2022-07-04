def solution(s):
    arr = s.split(' ')
    arr1=[]
    
    for i in range(len(arr)):
        a=[]
        for j in range(len(arr[i])):
            if j%2==0:
                a += arr[i][j].upper()
            else:
                a += arr[i][j].lower()
        arr1.append(''.join(a))
    return ' '.join(arr1)