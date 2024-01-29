import sys

def floid():
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    INF = int(1e9)
    graph = [[INF]*(n+1) for _ in range(n+1)]
    # 같은 값은 0 넣기(미러링 생각)
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a == b:
                graph[a][b] = 0
    # 입력받은 비용을 비교해 작으면 업데이트
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        if c < graph[a][b]:
            graph[a][b] = c
    # 순회하며 직빵이 짧은지 경유가 짧은지 비교
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    # 출력
    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][b] == INF:
                print(0, end=" ")
            else:
                print(graph[a][b], end=" ")

        print()

floid()