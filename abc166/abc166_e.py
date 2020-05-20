#!/usr/local/bin/python3

from sys import stdin
import sys
import math

##
# N
# A1
# A2
# AN
N = int(input())
A = [int(input()) for i in range(n)]
# or
N = int(stdin.readline().rstrip())
for i in range(N):
    A.append(stdin.readline().rstrip().split())

##
# N M
N, M = list(map(int, stdin.readline().rstrip().split()))

##
# A1 A2 ... An
## 配列に読み込む
A= stdin.readline().rstrip().split()
## それを int にキャスト
A = list(map(int, stdin.readline().rstrip().split()))
