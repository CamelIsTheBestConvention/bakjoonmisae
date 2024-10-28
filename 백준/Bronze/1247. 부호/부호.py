import sys

input = sys.stdin.readline

for i in range(3):
    n = int(input())
    total = 0
    for j in range(n):
        num = int(input())
        total += num

    if total > 0:
        print("+")
    elif total < 0:
        print("-")
    else:
        print("0")
