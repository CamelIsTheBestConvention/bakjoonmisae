import sys
input = sys.stdin.readline

def daeching(a, b):
    zip1 = set(map(int, input().split()))
    zip2 = set(map(int, input().split()))

    print(len(zip1-zip2) + (len(zip2-zip1)))

a, b = list(map(int, input().split()))
daeching(a, b) 