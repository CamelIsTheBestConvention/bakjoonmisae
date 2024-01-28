import sys

n, m = list(map(int, sys.stdin.readline().split()))
burket = [0] * n

for cnt in range(m):
    i, j, k = list(map(int, sys.stdin.readline().split()))

    for cnt2 in range(i-1, j):
        burket[cnt2] = k

print(*burket)
