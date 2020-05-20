#!/usr/local/bin/python3

from sys import stdin
import math


[K, S] = list(map(int, stdin.readline().rstrip().split()))

count=0

for x in range(K+1):
    for y in range(K+1):
        if x + y > S:
            continue
        if S - (x + y) <= K:
            #print("%d %d %d" % (x, y, S-(x+y)))
            count = count + 1

print(count)

