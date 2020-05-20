#!/usr/local/bin/python3

from sys import stdin

n = int(stdin.readline().rstrip())
data=[]
for i in range(0, n):
    data.append(int(stdin.readline().rstrip()))

print(len(set(data)))
