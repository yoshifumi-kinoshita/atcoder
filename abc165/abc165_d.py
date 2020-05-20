#!/usr/local/bin/python3

from sys import stdin
import sys
import math

A, B, N = list(map(int, stdin.readline().rstrip().split()))

ans = []

if B <= N:
    x = B - 1
    while x <= N:
        x += B
        ans.append(math.floor(A * x / B) - A * math.floor(x / B))
    print(max(ans))
else:
    print(math.floor(A * N / B) - A * math.floor(N / B))

