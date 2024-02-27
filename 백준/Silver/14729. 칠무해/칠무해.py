import sys
import heapq
input = sys.stdin.readline

def SevenBumbu():
    n = int(input().rstrip())

    sevenNewbi = []

    for _ in range(7):
        input_value: float = float(sys.stdin.readline().rstrip())
        heapq.heappush(sevenNewbi, input_value * -1)

    for _ in range(n - 7):

        max_value = sevenNewbi[0] * -1
        input_value: float = float(sys.stdin.readline().rstrip())

        if max_value > input_value:
            heapq.heapreplace(sevenNewbi, input_value * -1)

    sevenNewbi.sort(reverse=True)

    for score in sevenNewbi:
        print(f'{score * -1:.3f}')

SevenBumbu()