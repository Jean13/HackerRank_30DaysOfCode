import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
# reverse, unpack arguments out of list, print
print(*reversed(arr))
