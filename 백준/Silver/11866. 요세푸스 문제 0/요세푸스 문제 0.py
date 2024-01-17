import sys

# n[0] = 인원 수, n[1] = 제거할 간격
n = list(map(int, sys.stdin.readline().split()))
arr = []
# 인덱스 시작이 1이기 때문에 제거될 위치에서 1 깎아주기
cnt = n[1] - 1
result = []

# [1, 2, 3, 4, 5, 6, 7]
for i in range(1, n[0]+1):
    arr.append(i)

# 배열을 무한으로 돌며 배열의 길이가 cnt보다 작아지면 cnt의 나머지값을 넣고 다시 진행
while arr:
    if cnt >= len(arr):
        cnt = cnt % len(arr)

    # result에 cnt값 자리의 값을 삭제 후 result로 이동
    result.append(arr.pop(cnt))
    cnt += n[1]-1

jjin_result = '<' + ", ".join(map(str, result)) + '>'
print(jjin_result)