#!/usr/local/bin/python3

from sys import stdin
import sys
import math

S, W = list(map(int, stdin.readline().rstrip().split()))

if S <= W:
    print('unsafe')
else:
    print('safe')


