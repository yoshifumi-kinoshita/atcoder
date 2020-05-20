#!/usr/local/bin/python3

from sys import stdin
import sys
import math

N = int(input())
A = [int(input()) for i in range(N)]

h = {}

for i in A:
    h[i] = 0

for j in A:
    h[j] += 1


count = 0
for val in h.values():
    if val % 2 == 1:
        count += 1

print(count)
