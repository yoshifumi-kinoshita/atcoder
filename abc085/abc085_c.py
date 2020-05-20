#!/usr/local/bin/python3

from sys import stdin
import sys

(N, Y) = stdin.readline().rstrip().split()

N = int(N)
Y = int(Y)

## 1 <= N <= 2000
## 1000 <= Y <= 2 * 10**7

## x y z
## x 10000
## y 5000
## z 1000

## N == x + y + z
## Y == 10000 * x + 5000 * y + 1000 * z


for x in range(0, N+1):
    if 10000 * x > Y:
        break
    if 10000 * x + 5000 * N-x < Y:
        continue
    for y in range(0, N+1 - x ):
        if 10000 * x + 5000 * y > Y:
            break
        #print("total:%d 10000:%d 5000:%d 1000:%d" % (10000 * x + 5000 * y + 1000 * z, x, y, z))
        z = N - x - y
        if (Y == 10000 * x + 5000 * y + 1000 * z) and (N == x + y + z):
                print("%d %d %d" % (x, y, z))
                sys.exit()

print('-1 -1 -1')


