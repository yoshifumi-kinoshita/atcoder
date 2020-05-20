#!/usr/local/bin/python3

from sys import stdin
import sys
import math

A, B, C, D = list(map(int, stdin.readline().rstrip().split()))

while A > 0 and C > 0:
    C -= B
    if C <= 0:
        print('Yes')
        sys.exit()

    A -= D
    if A <= 0:
        print('No')
        sys.exit()


