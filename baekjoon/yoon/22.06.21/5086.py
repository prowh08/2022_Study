while True:
    n,m = map(int,input().split())
    if n==0 and m==0:
        break
    else:
        if m%n ==0:
            print('factor')
        elif n%m ==0:
            print('multiple')
        elif n%m !=0 and m%n!=0:
            print('neither')

