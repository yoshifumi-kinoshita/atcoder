#!/usr/local/bin/python3

from sys import stdin

[N, X] = list(map(int, stdin.readline().rstrip().split()))
m = [int(input()) for i in range(N)]

m_sorted = sorted(m)

for i in range(N):
    X = X - m[i]

print(len(m) + X // m_sorted[0])



