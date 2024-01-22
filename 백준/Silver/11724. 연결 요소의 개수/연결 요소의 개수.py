import sys


def line_connect(n, visited, line):
    # 방문확인을 true값으로 변경
    visited[n] = True

    # 노드배열을 돌며 방문이 false인 곳이 있으면 재귀를 돌려 true로 변경
    for i in line[n]:
        if not visited[i]:
            line_connect(i, visited, line)

# 노드 n, 간선 m, 방문확인 전부 false, 선 연결 배열 빈배열로 만들기line, 요소 개수c
n, m = map(int, sys.stdin.readline().split())
visited = [False] * (n+1)
line = [[] for _ in range(n+1)]
cnt = 0

# 간선의 개수만큼 a, b에 노드 입력, 노드1에 5가 연결이면 5에도 1이 연결되야 하기 때문에 둘다 적용
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    line[a].append(b)
    line[b].append(a)

# 모든 노드를 반복하며 방문이 안된 노드가 있으면 cnt를 1 증가
for i in range(1, n+1):
    if not visited[i]:
        line_connect(i, visited, line)
        cnt += 1

print(cnt)

