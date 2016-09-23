import sys


N = int(input().strip())

for i in range(1,11):
    print(N, "x", i, "=", N * i)
    i+= i

