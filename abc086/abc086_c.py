#!/usr/local/bin/python3

from sys import stdin
import sys

data = []

N = int(stdin.readline().rstrip())
for i in range(0, N):
    data.append(stdin.readline().rstrip().split())

cur_t = 0
cur_x = 0
cur_y = 0

for i in range(0, len(data)):
    (next_t, next_x, next_y) = data[i]
    next_t = int(next_t)
    next_x = int(next_x)
    next_y = int(next_y)

    sub_t = next_t - cur_t
    sub_x = abs(next_x - cur_x)
    sub_y = abs(next_y - cur_y)

    if sub_t < sub_x + sub_y:
        print('No')
        sys.exit()

    if sub_t % 2 != (sub_x + sub_y)%2:
        print('No')
        sys.exit()

    cur_t = next_t
    cur_x = next_x
    cur_y = next_y

print('Yes')

