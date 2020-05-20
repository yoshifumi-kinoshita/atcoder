#!/usr/local/bin/python3

from sys import stdin

(n, a, b) = stdin.readline().rstrip().split()
n = int(n)
a = int(a)
b = int(b)

total=0
POW_MAX=4

for i in range(1, n+1):
    sub_total=0
    num = i
    for j in range(0, POW_MAX+1):

        mod = num % 10
        sub_total = sub_total + mod
        sho = num // 10
        num = sho
        if sho == 0:
            break
    if a <= sub_total and sub_total <= b:
        print("n:%d sub_total:%d" % (i, sub_total))
        total = total + i

print(total)



