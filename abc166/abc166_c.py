#!/usr/local/bin/python3

from sys import stdin
import sys
import math


N, M = list(map(int, stdin.readline().rstrip().split()))
H = list(map(int, stdin.readline().rstrip().split()))

A = []
for i in range(M):
    #A.append(stdin.readline().rstrip().split())
    A.append(list(map(int, stdin.readline().rstrip().split())))

#print(H)
#print(A)

m = {}

for tmp in A:
    #print(tmp)
    a, b = tmp
    #print(a)
    if H[a - 1] > H[b - 1]:
        m[b] = 0
    elif H[a - 1] < H[b - 1]:
        m[a] = 0
    else:
        m[a] = 0
        m[b] = 0

count = 0
for j in range(1, N+1):
    if m.get(j, 1) == 1:
        count += 1

print(count)
