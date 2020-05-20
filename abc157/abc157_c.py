#!/usr/local/bin/python3

from sys import stdin
import sys
import math

N, M = list(map(int, stdin.readline().rstrip().split()))
S = []
h = {}
for i in range(M):
    s, c = list(map(int, stdin.readline().rstrip().split()))
    S.append([s, c])

ans = 999
for i in range(1000)[::-1]:
    s = str(i)
    for key, val in h.items():
        if h[h-1] == val
