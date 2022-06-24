n=int(input())
q,c=0,0
q=n//10
c=n//125+n//25
print(q*2+c if n%10<5 else q*2+c+1)