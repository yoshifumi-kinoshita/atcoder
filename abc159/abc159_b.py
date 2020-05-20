#!/usr/local/bin/python3

from sys import stdin
import sys
import math

# S は回文である。
# N を S の長さとするとき、 S の 1 文字目から ( N − 1) / 2 文字目まで(両端含む)からなる文字列は回文である。
# S の ( N + 3) / 2 文字目から N 文字目まで(両端含む)からなる文字列は回文である。

S = input()

def is_kaibun(s):
    for i in range(len(s) // 2 + 1):
        if s[i] != s[-(i + 1)]:
            return False
    return True

def is_half_kaibun(s):
    s = s[0:len(s)//2]
    return is_kaibun(s)

if is_kaibun(S) and is_half_kaibun(S):
    print('Yes')
else:
    print('No')



