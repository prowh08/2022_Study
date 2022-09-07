from math import factorial
import sys
input = sys.stdin.readline

def two_cnt(n):
    two = 0
    while n!=0:
        n = n // 2
        two += n
    return two

def five_cnt(n):
    five = 0
    while n!=0:
        n = n // 5
        five += n
    return five

n, m = map(int, input().split())
# n! / ((n-m)! * m!)
print(min(two_cnt(n)-two_cnt(n-m)-two_cnt(m), five_cnt(n)-five_cnt(n-m)-five_cnt(m)))
