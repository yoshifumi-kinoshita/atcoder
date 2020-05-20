#!/usr/local/bin/python3

from sys import stdin
import sys
import math

def isOdd(n):
    return n % 2 == 1

def isPair(n):
    return n % 2 == 0


A, B, C = list(map(int, stdin.readline().rstrip().split()))

l, m, n = sorted([A, B, C], reverse=True)

count = 0


while l > m or l > n:
    if isOdd(l) and isOdd(m) and isPair(n) or isPair(l) and isPair(m) and isOdd(n):
        l += 1
        m += 1
        count += 1
    elif isOdd(l) and isPair(m) and isOdd(n) or isPair(l) and isOdd(m) and isPair(n):
        l += 1
        n += 1
        count += 1
    elif isPair(l) and isOdd(m) and isOdd(n) or isOdd(l) and isPair(m) and isPair(n):
        m += 1
        n += 1
        count += 1
    else:
        if l > m:
            count += (l - m) // 2
            m += (l - m)
        if l > n:
            count += (l - n) // 2
            n += (l - n)

print(count)



