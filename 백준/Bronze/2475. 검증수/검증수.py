import sys
input = sys.stdin.readline

num = list(map(int, input().split()))
result = 0

for n in num:
    result += n*n

result = result % 10
print(result)