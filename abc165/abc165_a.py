#!/usr/local/bin/python3

from sys import stdin
import sys
import math

N = int(input())
A, B = list(map(int, stdin.readline().rstrip().split()))


for i in range(A, B+1):
    if i % N == 0:
        print('OK')
        sys.exit()
print('NG')

