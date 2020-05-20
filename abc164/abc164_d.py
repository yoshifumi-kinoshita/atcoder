#!/usr/local/bin/python3

#from sys import stdin

#S = int(input())
S = input()

# 1<=S<=21

def find2019(s):
    print(s)
    #for e in range(4, len(s)+1):
    for e in range(5, len(s)+1):
        res = int(s[0:e]) % 2019
        if res == 0:
            #print(s)
            #print(s[0:e])
            return True
    return False

count = 0
for i in range(0, len(S)-4):
    if sum([int(i) for i in list(S[i:])]) % 3 == 0:
        if find2019(S[i:]):
            count += 1
print(count)


