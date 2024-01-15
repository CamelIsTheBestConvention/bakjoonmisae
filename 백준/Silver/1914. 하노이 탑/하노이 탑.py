import sys

def hanoi(n, start, sub, finish):
    if n == 1:
        print(start,finish)
    else:
        hanoi(n-1, start, finish, sub)
        print(start, finish)
        hanoi(n-1, sub, start, finish)


n = int(sys.stdin.readline())

print(2**n-1)
if n<=20:
    hanoi(n, '1', '2', '3')