#!/usr/local/bin/python3

from sys import stdin
import sys
import math

[N, C, K] = list(map(int, stdin.readline().rstrip().split()))
T = sorted([int(input()) for i in range(N)])

print(T)

bus = 1
passenger = 0
first_passengers_time = -1
for i in T:
    print("%d %d" % (bus, i))
    if passenger == C or (passenger > 0 and first_passengers_time + K < i):
        bus += 1
        passenger = 0
        first_passengers_time = 0

    if passenger == 0:
        passenger += 1
        first_passengers_time = i
    elif passenger < C and first_passengers_time + K >= i:
        passenger += 1

print(bus)


