import sys
input = sys.stdin.readline

n = int(input())
word = list(input().strip())
hiddenNum = ''
result = 0

for i in range(n):
    if word[i].isdigit():
        hiddenNum += word[i]
    else:
        if hiddenNum:
            result += int(hiddenNum)
            hiddenNum = ''

if hiddenNum:
    result += int(hiddenNum)

print(result)