#!/usr/local/bin/python3

from sys import stdin
import sys
import math

N = int(input())

def f(a, b):
    return len(str(max(a, b)))

minimum = float('inf')

for a in range(1, int(math.sqrt(N))+1):
    if N % a == 0:
        minimum = min(minimum, f(a, N // a))

print(minimum)

