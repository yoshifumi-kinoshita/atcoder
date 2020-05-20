#!/usr/local/bin/python3

from sys import stdin
import math


N = int(stdin.readline().rstrip())

def sum_of_digit(n):
    total = 0
    s = str(n)
    for i in range(len(s)):
        total = total + int(s[i:i+1])

    return total


def isHarshad(n):
    return n % sum_of_digit(n) == 0

if isHarshad(N):
    print("Yes")
else:
    print("No")

