#!/usr/local/bin/python3

from sys import stdin

N = int(stdin.readline().rstrip())
#A = stdin.readline().rstrip().split()
#A = stdin.readline().rstrip().split()
#print(A)
#data = list(map(int, A))
A = list(map(int, stdin.readline().rstrip().split()))
#print(data)

print(max(A) - min(A))


