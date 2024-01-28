import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
find = int(sys.stdin.readline())
cnt = 0

for i in nums:
    if i == find:
        cnt += 1

print(cnt)