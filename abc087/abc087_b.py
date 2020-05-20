#!/usr/local/bin/python3

from sys import stdin

a = int(stdin.readline().rstrip())
b = int(stdin.readline().rstrip())
c = int(stdin.readline().rstrip())
x = int(stdin.readline().rstrip())
x_500_100_50 = x

total=0


## 500
for i in range(0, a+1):
    if i * 500 > x_500_100_50:
        break
    #if i * 500 == x_500_100_50:
    #    total = total + 1
    x_100_50 = x_500_100_50 - i * 500

    ## 100
    for j in range(0, b+1):
        if j * 100 > x_100_50:
            break
        #if j * 100 == x_100_50:
        #    total = total + 1
        x_50 = x_100_50 - j * 100

        ## 50
        for k in range(0, c+1):
            if k * 50 > x_50:
                break
            if k * 50 == x_50:
                total = total + 1
                #print("500: %d  100: %d  50: %d" % (i, j, k))

print(total)

