#!/usr/local/bin/python3

from sys import stdin
import sys
import math

N, M = list(map(int, stdin.readline().rstrip().split()))



odd_nums = [i for i in A if i % 2 ==1]

if len(odd_nums) % 2 == 0:
    print("YES")
else:
    print("NO")
