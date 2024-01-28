import sys

n = int(sys.stdin.readline())
long = []

for i in range(0, n, 4):
    long.append('long')

print(" ".join(long), 'int')