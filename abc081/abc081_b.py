#!/usr/local/bin/python3

from sys import stdin

n = int(stdin.readline().rstrip())
data = stdin.readline().rstrip().split()

i=0

while True:
    for num in data:
        if int(num) % (2 ** i) > 0:
            print(i-1)
            exit(0)
    i = i + 1

