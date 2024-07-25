import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, h):
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > h and not visited[nx][ny]:
                visited[nx][ny] = True
                stack.append((nx, ny))

total_cnt = 0

for h in range(101):
    cnt = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if arr[j][k] > h and not visited[j][k]:
                dfs(j, k, h)
                cnt += 1
    total_cnt = max(total_cnt, cnt)

print(total_cnt)