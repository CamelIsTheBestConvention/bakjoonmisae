import sys

n, m = list(map(int, sys.stdin.readline().split()))
tree_heights = list(map(int, sys.stdin.readline().split()))

start, end = 1, max(tree_heights)

# 검색 트리의 최대를 가장 긴 나무로 잡기
while start <= end:
    # 톱으로 자를 위치를 중간으로 잡기
    mid = (start + end) // 2
    # 나무들의 길이에서 중간을 뺸 값이
    # 0보다 크면 뺸 값을 cut_tree에 넣기
    # 0보다 작으면 넣지 말기
    cut_tree = 0
    for height in tree_heights:
        if height - mid > 0:
            cut_tree += height - mid
        else:
            cut_tree += 0
    
    # 만약 자르는 값이 자른 나무보다 적으면 start값을 중간 위로 올리기 
    if cut_tree >= m:
        start = mid + 1
    # 자르는 값이 자른 나무보다 많으면 start값을 중간 밑으로 내리기
    else:
        end = mid - 1

print(end)