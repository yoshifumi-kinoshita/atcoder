#!/usr/local/bin/python3

from sys import stdin
import sys
import math

N, M, Q = list(map(int, stdin.readline().rstrip().split()))
a = []
for i in range(Q):
    a.append(stdin.readline().rstrip().split())

#print(A)

## A = {1, 3, 4}
#
# 3 4 3
# 1 3 3 100
# A{3} - A{1} == 3
# 
# 1 2 2 10
# A{2} - A{1} == 2
#
# 2 3 2 10
# A{3} - A{2} != 2

#for array in a:
    #print(array)


for n in range(2, N+1):
    test = []
    for m in range(1, M+1):
        test.append(m)
    print(test)


