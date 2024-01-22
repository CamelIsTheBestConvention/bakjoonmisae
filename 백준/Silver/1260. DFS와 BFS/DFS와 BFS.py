from collections import deque
import sys

# 깊이 우선 탐색
def dfs(graph, v, visited):
    # 방문확인을 True로 하고 시작노드인 v 출력
    visited[v] = True
    print(v, end=' ')
    # 시작노드의 연결노드를 확인해서 만약 방문 안한 노드가 있으면
    for i in graph[v]:
        if not visited[i]:
            # 재귀 시작
            dfs(graph, i, visited)

# 너비 우선 탐색
def bfs(graph, start, visited):
    # 데큐를 이용해 시작노드를 큐에 저장
    queue = deque([start])
    # 시작노드의 방문확인을 True로 하고
    visited[start] = True
    # 큐가 없을 때까지 무한 반복을 돌려서 
    while queue:
        # 큐는 맨 앞에 있는 값부터 차례대로 뺴기 떄문에
        # 앞의 걸 뺴는 popleft 데큐 기능 사용
        v = queue.popleft()
        print(v, end=' ')
        # 시작노드의 연결노드를 확인해서 만약 방문 안한 노드가 있으면
        for i in graph[v]:
            if not visited[i]:
                # 큐에 넣고 방문확인을 True로 변경
                queue.append(i)
                visited[i] = True

# 노드 개수(n), 간선 개수(m), 시작 노드(v)
n, m, v = map(int, sys.stdin.readline().split())
# 각 노드별로 연결된 부분을 찾기 위해 빈 2차원배열 생성
graph = [[] for _ in range(n+1)]
# 방문유무를 노드개수+1해서 0번쨰는 사용하지않고 1번째부터 사용
visited = [False] * (n+1)

# 입력된 노드연결을 입력해야해서 간선의 수만큼 반복
for _ in range(m):
    # 시작노드 a, 연결노드 b 받고 양방향 그래프이기 때문에 둘다 값 추가
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 노드마다 연결된 노드 리스트를 오름차순으로 정렬
for i in range(n+1):
    graph[i].sort()

# 깊이우선탐색(노드연결리스트, 시작 노드, 방문확인)
dfs(graph, v, visited)
# 너비우선탐색을 위해 방문확인 다시 초기화하고 띄어쓰기 위해 공백출력
visited = [False] * (n+1)
print()
# 너비우선탐색(노드연결리스트, 시작 노드, 방문확인)
bfs(graph, v, visited)

