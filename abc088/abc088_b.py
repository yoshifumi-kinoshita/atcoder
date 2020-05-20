#!/usr/local/bin/python3

from sys import stdin

n = int(stdin.readline().rstrip())
data = stdin.readline().rstrip().split()

data = sorted(data, key=int, reverse=True)

alice_total=0
bob_total=0


for i in range(0, n):
    if i % 2 == 0:
        alice_total = alice_total + int(data[i])
    else:
        bob_total = bob_total + int(data[i])

print(alice_total - bob_total)


