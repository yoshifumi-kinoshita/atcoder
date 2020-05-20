#!/usr/local/bin/python3

from sys import stdin
import math

[N, L] = list(map(int, stdin.readline().rstrip().split()))
#S = [int(input()) for i in range(N)]
S = [input() for i in range(N)]

S_sorted = sorted(S)

print(''.join(S_sorted))

