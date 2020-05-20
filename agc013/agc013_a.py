#!/usr/local/bin/python3

from sys import stdin
import sys
import math

N = int(stdin.readline().rstrip())
A = list(map(int, stdin.readline().rstrip().split()))

ASC = -1
DESC = 1

flag_asc_desc = 0
count = 1
prev = 0
for i in A:
    if prev == 0:
        prev = i
        flag_asc_desc = 0
        continue
    
    if flag_asc_desc == ASC and i >= prev:
        prev = i
        continue
    elif flag_asc_desc == ASC and i < prev:
        prev = i
        flag_asc_desc = 0
        count += 1
    elif flag_asc_desc == DESC and i <= prev:
        prev = i
        continue
    elif flag_asc_desc == DESC and i > prev:
        prev = i
        flag_asc_desc = 0
        count += 1
    elif i == prev:
        prev = i
        continue
    elif i < prev:
        flag_asc_desc = DESC
        prev = i
    elif i > prev:
        flag_asc_desc = ASC
        prev = i
    else:
        print("error")

print(count)
