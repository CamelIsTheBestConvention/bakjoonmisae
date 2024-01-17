# n개의 탑은 각각 왼쪽에 신호를 쏘는데 왼쪽에 본인보다 큰 탑에만 수신이 가능하다
# 각 탑마다 누가 신호를 받는지 출력
import sys

# 탑의 개수 n, n개만큼 리스트로 탑을 받는다
n = int(sys.stdin.readline())
tower = list(map(int, sys.stdin.readline().split()))
# 스택 구현 배열과 탑이 신호를 받을 탑이 있는지 확인하는 result
stack = []
result = [0] * n

# 
for i in range(n):
    # 스택에 값이 있고 가장 마지막에 있는 tower가 i번째 값보다 낮을 때
    while stack and tower[stack[-1]] < tower[i]:
        # 맨 위의 값을 제거
        stack.pop()
    # 스택에 값이 없으면 i번째 result 값을 1로 변경한다
    if stack:
        result[i] = stack[-1] + 1
    # stack리스트에 result를 추가
    stack.append(i)

# split()과 다르게 여러 출력값을 붙여서 출력
print(' '.join(map(str, result)))
