#!/usr/local/bin/python3

from sys import stdin
import sys
import math

X = int(input())

year = 0
total = 100

while True:
    year += 1
    total += math.floor(total * 1 / 100)
    if total >= X:
        print(year)
        sys.exit()


