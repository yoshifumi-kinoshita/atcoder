#!/usr/local/bin/python3

from sys import stdin
import sys

N = int(input())
S = [input() for i in range(N)]

M = int(input())
T = [input() for i in range(M)]

#print(S)
#print(T)

words_count = {}
for i in range(N):
    words_count[S[i]] = words_count.get(S[i], 0) + 1

for i in range(M):
    words_count[T[i]] = words_count.get(T[i], 0) - 1

#print(words_count)
#print(max(words_count, key=lambda x:x[1]))
print(max(0, max(words_count.values())))
