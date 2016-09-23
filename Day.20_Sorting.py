#!/bin/python3

import sys


n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
numSwaps = 0

for i in range(n):
    for j in range(n-1-i):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
            numSwaps += 1

print("Array is sorted in {} swaps.\nFirst Element: {}\nLast Element: {}".format(numSwaps, a[0], a[-1]))

