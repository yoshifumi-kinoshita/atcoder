#!/usr/local/bin/python3

from sys import stdin
import sys
import math

N, K = list(map(int, stdin.readline().rstrip().split()))

d = []
A = []
n = {}
for i in range(K):
    d.append(int(input()))
    #A.append(stdin.readline().rstrip().split())
    tmp = list(map(int, stdin.readline().rstrip().split()))
    A.append(tmp)
    for a in tmp:
        n[a] = 1

count = 0
for j in range(1, N+1):
    if n.get(j, 0) == 0:
        count += 1

print(count)


#print(d)
#print(A)
#print(n)



