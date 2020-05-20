#!/usr/local/bin/python3

from sys import stdin
import math

N, K = list(map(int, stdin.readline().rstrip().split()))
B = 10**100

n = [i for i in range(0, N+1)]

amount_min = 0
for j in range(K):
    amount_min += n[j]

#print(amount_min)


amount_max = 0
for k in range(N+1):
    amount_max += k

#print(amount_max)

count = (amount_max - amount_min)
count = 

#print(count)
print(count % (10**9+7))

