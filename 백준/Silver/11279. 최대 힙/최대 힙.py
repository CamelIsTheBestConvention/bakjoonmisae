import heapq
import sys

# 총 몇개를 입력받을지 n값에 담기
n = int(sys.stdin.readline())
# 리스트값을 담을 배열
heap = []

# n만큼 반복하면서 price 변수에 입력값 하나씩 집어넣기
for i in range(n):
    price = int(sys.stdin.readline())
    # 입력값이 0일 때 heap배열의 정수가 없으면 0을 출력
    if price == 0:
        if len(heap) == 0:
            print(0)
        # 그게 아니라면 힙에서 원소를 하나 제거하고 원래 값을 출력
        else:
            print(heapq.heappop(heap)[1])
    # 입력값이 0이 아니라면 [-x, x]방식으로 값을 넣는다
    # 힙 라이브러리는 최소 힙을 구현하기 때문에 가장 작은 값이 위치해야 하는데
    # 최대 힙을 구해야 하는 문제기 떄문에 -를 줘서 작은 값이 우선순위를 가지게 되어
    # x보다 -x가 먼저 위치하게 된다.
    else:
        heapq.heappush(heap, [-price, price])