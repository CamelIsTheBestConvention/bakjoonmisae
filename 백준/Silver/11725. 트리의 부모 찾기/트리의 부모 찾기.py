n = int(input())
edges = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

visited = [False] * (n+1)
mom = [0] * (n+1)

stack = [1]  # 시작 노드인 1을 스택에 추가

while stack:
    v = stack.pop()  # 스택에서 노드를 하나 꺼냄

    if not visited[v]:
        visited[v] = True

        for i in edges[v]:
            if not visited[i]:
                mom[i] = v
                stack.append(i)  # 자식 노드를 스택에 추가

for i in range(2, n+1):
    print(mom[i])