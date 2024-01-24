# 1번 줄 테스트 케이스 개수 k
# 2번 줄 정점v, 간선개수e 입력
# 3번 줄 부터 간선을 이루는 두 정점 u, v 입력
import sys
sys.setrecursionlimit(10**4)
# 테스트 케이스 k
k = int(sys.stdin.readline())
# k만큼 반복 : 정점v, 간선개수 e

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

def binary_graph(k):
    for _ in range(k):
        v, e = list(map(int, sys.stdin.readline().split()))
        visited = [False] * (v+1)
        graph = [[] for _ in range(v+1)]
        color = [False] * (v+1)

        for _ in range(e):
            a, b = list(map(int, sys.stdin.readline().split()))
            graph[a].append(b)
            graph[b].append(a)
            
        is_bipartite = True
        for i in range(1, v+1):
            if not visited[i]:
                if not dfs(graph, i, visited, color):
                    is_bipartite = False
                    break

        print("YES" if is_bipartite else "NO")

binary_graph(k)


