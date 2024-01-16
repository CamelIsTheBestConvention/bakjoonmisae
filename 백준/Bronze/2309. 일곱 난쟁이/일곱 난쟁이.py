from itertools import combinations

arr = []

for i in range(9):
    arr.append(int(input()))

# combinations라는 기능을 이용해 7개의 숫자를 경우의 수가 되는대로 전부 담기
find = list(combinations(arr, 7))

# 경우의 수 안에서 7개 값이 100개일 경우 list타입으로 바꾸어 arr에 담기
for i in find:
    if sum(i) == 100:
        arr = list(i)

# arr을 정렬시키고 출력
arr.sort()

for i in range(len(arr)):
    print(arr[i])