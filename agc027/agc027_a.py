#!/usr/local/bin/python3

from sys import stdin
import math

[N, x] = list(map(int, stdin.readline().rstrip().split()))
a = list(map(int, stdin.readline().rstrip().split()))

a_sorted = sorted(a)


count=0
for i in range(N):
    #x -= a_sorted[i]
    x = x - a_sorted[i]
    if x >=0:
        count += 1
    else:
        break

if x > 0:
    count -= 1

print(count)



