import sys
input = sys.stdin.readline

a = 0

for i in range(4):
	a += int(input())
    
print(a // 60)
print(a % 60)