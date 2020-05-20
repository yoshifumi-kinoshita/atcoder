#!/usr/local/bin/python3

from sys import stdin
import sys

[W, H, N] = list(map(int, stdin.readline().rstrip().split()))


Ws = 0
We = W

Hs = 0
He = H


A = []
for i in range(N):
    A.append(list(map(int, stdin.readline().rstrip().split())))

for i in range(N):
    [x, y, a] = A[i]
    if a == 1:
        Ws = max(Ws, x)
    elif a == 2:
        We = min(We, x)
    elif a == 3:
        Hs = max(Hs, y)
    elif a == 4:
        He = min(He, y)

if (We - Ws) <= 0 or (He - Hs) <=0:
    print(0)
else:
    print((We - Ws) * (He - Hs))



