import sys

n, k = list(map(int, sys.stdin.readline().split()))
money = []
cnt = 0
exchange = []

for i in range(n):
    money.append(int(sys.stdin.readline()))

for i in range(n):
    exchange = money.pop()
    if k / exchange < 0:
        continue
    else:
        cnt += k // exchange
        k = k % exchange
print(cnt)