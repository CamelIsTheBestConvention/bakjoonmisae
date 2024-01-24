# 1번 줄 테스트 케이스 개수 k
# 2번 줄 정점v, 간선개수e 입력
# 3번 줄 부터 간선을 이루는 두 정점 u, v 입력
import sys
# 재귀함수 최대 10000번
sys.setrecursionlimit(10**4)

# 테스트 케이스 k
k = int(sys.stdin.readline())

# 깊이 탐색 함수
def dfs(graph, v, visited, color):
    visited[v] = True

    for i in graph[v]:
        if visited[i]:
            if color[i] == color[v]:
                return False
        else:
            color[i] = not color[v]
            if not dfs(graph, i, visited, color):
                return False
    return True

# 이분 그래프 함수
def binary_graph(k):
    # k만큼 반복 : 정점v, 간선개수 e, 방문확인 visited, 간선정보 graph, 색깔비교 color
    for _ in range(k):
        v, e = list(map(int, sys.stdin.readline().split()))
        visited = [False] * (v+1)
        graph = [[] for _ in range(v+1)]
        color = [False] * (v+1)

        # 간선 갯수만큼 반복하여 a, b에 시작노드, 끝노드 넣고 각 연결노드 확인에 삽입
        for _ in range(e):
            a, b = list(map(int, sys.stdin.readline().split()))
            graph[a].append(b)
            graph[b].append(a)

        # 그래프를 확인하고 Yes를 출력할지 No를 출력할지 체크하는 변수
        YesNo = True
        # 1부터 정점+1까지 방문안한 노드가 있으면:
        for i in range(1, v+1):
            if not visited[i]:
                # 만약 dfs의 return값이 false라면 YesNo를 false로 바꾸고 빠져나오기
                if not dfs(graph, i, visited, color):
                    YesNo = False
                    break

        # 체크 변수에 따라 yes혹은 No 출력
        print("YES" if YesNo else "NO")

binary_graph(k)
