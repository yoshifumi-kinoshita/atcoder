#!/usr/local/bin/python3

from sys import stdin

N = int(stdin.readline().rstrip())
[T, A] = list(map(int, stdin.readline().rstrip().split()))
H = list(map(int, stdin.readline().rstrip().split()))



def temp(t, height):
    return t - height * 0.006

def difference(a, t):
    return max(a, t) - min(a, t)

nearest_point = 0
nearest_diff = 1000000

for i in range(N):
    t = temp(T, H[i])
    diff = difference(A, t)

    if nearest_diff > diff:
        nearest_point = i
        nearest_diff = diff

print(nearest_point+1)

