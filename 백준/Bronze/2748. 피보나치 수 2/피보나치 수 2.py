import sys

def fibo(n):
    list = [0, 1] + [0]*(n-1)

    for i in range(2, n+1):
        list[i] = list[i-1] + list[i-2]

    return list[n]

n = int(sys.stdin.readline())

print(fibo(n))