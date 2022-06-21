import sys
import math

a, b = map(int, sys.stdin.readline().split())
print(math.gcd(a, b))
print(math.lcm(a, b))