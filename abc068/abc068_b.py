#!/usr/local/bin/python3

from sys import stdin

N = int(stdin.readline().rstrip())

max_num = 1
max_count = 0

def division(n):
    count = 0
    while True:
        quo = n // 2
        rem = n % 2

        if quo == 0 or rem > 0:
            break
        else:
            count = count + 1

        n = quo

    return count


for i in range(1,N+1):
    count = division(i)
    if max_count < count:
        max_count = count
        max_num = i

print(max_num)
