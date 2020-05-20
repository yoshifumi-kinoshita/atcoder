#!/usr/local/bin/python3

from sys import stdin
import math

N = int(input())
S = input()


total = S.count('R') * S.count('G') * S.count('B')

for gap in range(1, N//2+1):
    for i in range(N - 2 * gap):
        j = i + gap
        k = j + gap
        if k >= N:
            continue
        if S[i] != S[j] and S[j] != S[k] and S[i] != S[k]:
            total -= 1

print(total)




