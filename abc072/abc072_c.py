#!/usr/local/bin/python3

from sys import stdin
import sys
import math

n = int(input())
a = list(map(int, stdin.readline().rstrip().split()))

dict_count = {}
for i in a:
    dict_count[i] = 0

for j in a:
    dict_count[j] += 1

#print(dict_count)

max_count = 0

for key in dict_count.keys():
    max_count = max(max_count, dict_count.get(key - 1, 0) + dict_count.get(key, 0) + dict_count.get(key + 1, 0))

print(max_count)

