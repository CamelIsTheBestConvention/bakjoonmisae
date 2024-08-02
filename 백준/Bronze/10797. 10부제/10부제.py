import sys
input = sys.stdin.readline

a = int(input())
cnt = 0

arr = list(map(int, input().split())) 

for i in arr:
    if a == i:
        cnt += 1

print(cnt)