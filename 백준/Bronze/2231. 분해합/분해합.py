import sys
input = sys.stdin.readline

n = int(input())
i = 1
sum = 0
    
while True:
    a = i
    sum = i
    while a > 0:
        sum = sum + (a % 10)
        a = a // 10
    if sum == n:
        print(i)
        break
    if i == n:
        print("0")
        break
    i += 1