import sys

# 입력값
n = int(sys.stdin.readline())
# 입력한 값의 1의 자리
a= 0
# 입력한 자릿수 합치는 값
sum = 0
# 우측 자리 합친 값
mix = n
# 사이클 카운트
cnt = 0

while True:
    if n == mix and cnt != 0:
        break
    else:
        a = mix % 10
        sum = (mix // 10) + (mix % 10)
        mix = int(str(a)+ str(sum % 10))
        cnt += 1
        

print(cnt)