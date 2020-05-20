#!/usr/local/bin/python3

from sys import stdin
import sys
import math

N = int(input())
A = list(map(int, stdin.readline().rstrip().split()))
print(A)

h = {}

for i in range(1, N+1):
    h[i] = 0

print(h)

for j in range(N-1):
    h[A[j]] += 1

print(h)

for val in h.values():
    print(val)

