#!/usr/local/bin/python3

from sys import stdin
import sys

N = int(stdin.readline().rstrip())

for i in range(26):
    if N < 4 * i:
        break
    if (N - 4 * i) % 7 == 0:
        print("Yes")
        sys.exit()


print("No")


