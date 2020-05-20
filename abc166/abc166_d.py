#!/usr/local/bin/python3

from sys import stdin
import sys
import math

X = int(input())

x = int(math.sqrt(X) + 1)

# ａ⁵－ｂ⁵＝(ａ－ｂ)(ａ⁴＋ａ³ｂ＋ａ²ｂ²＋ａｂ³＋ｂ⁴)
# a - b >= 1
# a != b


a5 = []
for i in range(1000):
    a5.append(i ** 5)

b5 = []
for j in range(1000):
    b5.append(j ** 5)

ans_a = 0
ans_b = 0

for a in a5:
    for b in b5:
        if a - b == X:
            print("%d %d" % (a5.index(a), b5.index(b)))
            sys.exit()
        elif a + b == X:
            print("%d %d" % (a5.index(a), -1 * b5.index(b)))
            sys.exit()

