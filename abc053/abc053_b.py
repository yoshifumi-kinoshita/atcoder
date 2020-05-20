#!/usr/local/bin/python3

from sys import stdin

s = stdin.readline().rstrip()

pos_a = s.find('A')
pos_z = s.rfind('Z')

print(pos_z - pos_a + 1)

