#!/usr/local/bin/python3

from sys import stdin
import math


[A, B] = list(map(int, stdin.readline().rstrip().split()))

def isKaibun(n):
    s = str(n)
    for i in range(len(s)//2):
        if s[i] == s[-(i+1)]:
            continue
        else:
            return False
    return True


count = 0
for i in range(A,B+1):
    if isKaibun(i):
        print(i)
        count = count + 1

print(count)


