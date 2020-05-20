#!/usr/local/bin/python3

from sys import stdin
import sys
import math

A, B = list(map(int, stdin.readline().rstrip().split()))

#x * 8 / 100 = A
#x * 10 / 100 = B

#xA = A * 100 / 8
#xB = B * 100 / 10


def tax(x,ratio):
    return math.floor(x * ratio / 100)


xA = int(A * 100 / 8)
xB = int(B * 100 / 10)

for i in range(max(0, xB-1), xA+10000):
    tax_a = tax(i, 8)
    tax_b = tax(i, 10)

    if tax_a == A and tax_b == B:
        print(i)
        sys.exit()

print(-1)

