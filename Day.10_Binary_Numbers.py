import sys


# For bin() function explanation, read: https://docs.python.org/3.5/library/functions.html#bin
print(len(max(bin(int(input().strip()))[2:].split('0'))))

