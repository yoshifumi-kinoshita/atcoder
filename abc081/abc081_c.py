#!/usr/local/bin/python3

from sys import stdin
import sys

[N, K] = list(map(int, stdin.readline().rstrip().split()))
A = list(map(int, stdin.readline().rstrip().split()))

h = {}
for i in range(N):
    if A[i] not in h:
        h[A[i]] = 0
    h[A[i]] += 1


count=0
num_of_items = len(h)

if num_of_items <= K:
    print(0)
    sys.exit()

for i in sorted(h.values()):
    if num_of_items > K:
        count += i
        num_of_items -= 1

print(count)

