import sys
input = sys.stdin.readline

t = int(input())
a, b, c = 300, 60, 10

aCount = t // a
t %= a

bCount  = t // b
t %= b

cCount = t // c
t %= c

if t == 0:
    print(aCount, bCount, cCount)
else:
    print(-1)
