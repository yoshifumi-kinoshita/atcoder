#!/usr/local/bin/python3

from sys import stdin
import sys

[N, M] = list(map(int, stdin.readline().rstrip().split()))

a = []
for i in range(M):
    a.append(list(map(int, stdin.readline().rstrip().split())))

print(a)

city = [[] for i in range(N+1)]

for i in range(M):
    [s, d] = a[i]
    city[s].append(d)
    city[d].append(s)

print(city)

for i in range(1, N+1):
    if len(city[i]) >= 0:
        print(len(city[i]))


