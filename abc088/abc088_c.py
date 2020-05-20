#!/usr/local/bin/python3

from sys import stdin
import sys

[c11, c12, c13] = list(map(int, stdin.readline().rstrip().split()))
[c21, c22, c23] = list(map(int, stdin.readline().rstrip().split()))
[c31, c32, c33] = list(map(int, stdin.readline().rstrip().split()))

#print("%d %d %d" % (c11, c12, c13))
#print("%d %d %d" % (c21, c22, c23))
#print("%d %d %d" % (c31, c32, c33))

## Horizontal
# 3*a1 + b1 + b2 + b3
# 3*a2 + b1 + b2 + b3
# 3*a3 + b1 + b2 + b3
# => 3 の倍数

## Vertical
# 3*b1 + a1 + a2 + a3
# 3*b2 + a1 + a2 + a3
# 3*b3 + a1 + a2 + a3
# => 3 の倍数

if ((c11 + c12 + c13) - (c21 + c22 + c23)) % 3 != 0 or ((c21 + c22 + c23) - (c31 + c32 + c33)) % 3 != 0 or ((c31 + c32 + c33) - (c11 + c12 + c13)) % 3 != 0:
    print("No")

elif ((c11 + c21 + c31) - (c12 + c22 + c32)) % 3 != 0 or ((c12 + c22 + c32) - (c13 + c23 + c33)) % 3 != 0 or ((c13 + c23 + c33) - (c11 + c21 + c31)) % 3 != 0:
    print("No")

else:
    print("Yes")



