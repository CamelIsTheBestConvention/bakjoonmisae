from collections import deque
import sys

def student_line(n, m, edges):
    line = [[] for _ in range(n+1)]
    count = [0] * (n+1)

    for edge in edges:
        a, b = edge
        line[b].append(a)
        count[a] += 1

    result = []
    queue = deque()

    for i in range(1, n+1):
        if count[i] == 0:
            queue.append(i)

    while queue:
        now = queue.popleft()
        result.append(now)

        for i in line[now]:
            count[i] -= 1

            if count[i] == 0:
                queue.append(i)

    return result

n, m = list(map(int, sys.stdin.readline().split()))
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

jjin_result = student_line(n, m, edges)
jjin_result.reverse()
print(*jjin_result)
