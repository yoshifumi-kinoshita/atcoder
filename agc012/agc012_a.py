#!/usr/local/bin/python3

from sys import stdin
import math

N = int(stdin.readline().rstrip())
a = list(map(int, stdin.readline().rstrip().split()))

a_sorted = sorted(a)
print( a_sorted )
total = 0
for i in range(N*1, N*3, 2):
    total += a_sorted[i]

print(total)


