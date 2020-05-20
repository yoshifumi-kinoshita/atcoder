#!/usr/local/bin/python3

import math

K = int(input())

amount = 0
for a in range(1, K+1):
    for b in range(1, K+1):
        gcd_ab = math.gcd(a, b)
        for c in range(1, K+1):
            amount += math.gcd(gcd_ab, c)

print(amount)

