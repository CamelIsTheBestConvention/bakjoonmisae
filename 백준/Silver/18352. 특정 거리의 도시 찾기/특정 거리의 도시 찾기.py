from collections import deque
import sys

def fine_city(line, x, visited, dist):
    queue = deque([x])
    visited[x] = True

    while queue:
        pop = queue.popleft()

        for i in line[pop]:
            if not visited[i]:
                queue.append(i)
                dist[i] = dist[pop] + 1
                visited[i] = True

    found = False
    for s in range(len(dist)):
        if dist[s] == k:
            print(s)
            found = True

    if not found:
        print(-1)

n, m, k, x = list(map(int, sys.stdin.readline().split()))

line = [[] for _ in range(n+1)]

visited = [False] * (n+1)

for i in range(m):
    a, b = list(map(int, sys.stdin.readline().split()))
    line[a].append(b)

dist = [0] * (n+1)

fine_city(line, x, visited, dist)
