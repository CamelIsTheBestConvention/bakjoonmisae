import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

n = int(input())
haveCard = sorted(list(map(int, input().split())))  # 정렬
m = int(input())
checkCard = list(map(int, input().split()))

sameCard = [1 if count_by_range(haveCard, card, card) > 0 else 0 for card in checkCard]

print(*sameCard)
