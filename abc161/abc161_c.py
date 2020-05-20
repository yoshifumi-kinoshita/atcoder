#!/usr/local/bin/python3

from sys import stdin
import math

N, K = list(map(int, stdin.readline().rstrip().split()))

mod = N % K

print(min(mod, abs(mod - K)))


