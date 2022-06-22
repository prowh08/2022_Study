from fractions import Fraction
import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
for i in range(1, len(l)):
    if Fraction(l[0], l[i])%1 == 0:
        print(str(Fraction(l[0], l[i]))+"/1")
    else:
        print(Fraction(l[0], l[i]))
