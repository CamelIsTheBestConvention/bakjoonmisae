import sys

N = int(sys.stdin.readline())
text = []

for i in range(N):
    text.append(sys.stdin.readline().strip())
# 중복 제거를 위해 set 사용
set_text = set(text)
text = list(set_text)

text.sort()
text.sort(key=len)
for i in range(len(text)):
    print(text[i])
