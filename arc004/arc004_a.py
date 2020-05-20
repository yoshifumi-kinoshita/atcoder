#!/usr/local/bin/python3

from sys import stdin
import math


N = int(stdin.readline().rstrip())

d = []
for i in range(N):
    d.append(list(map(int, stdin.readline().rstrip().split())))
X=0
Y=1

max_length_pow2 = 0

for i in range(len(d)):
    for j in range(len(d)):
        max_length_pow2 = max(math.pow(max(d[i][X], d[j][X]) - min(d[i][X], d[j][X]), 2) + math.pow(max(d[i][Y], d[j][Y]) - min(d[i][Y], d[j][Y]),2), max_length_pow2)

print(math.sqrt(max_length_pow2))





