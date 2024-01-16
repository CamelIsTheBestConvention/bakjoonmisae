import sys

n = int(input())
arr = []

# 입력값 받아 arr배열에 넣기
for i in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()

for i in arr:
    print(i)