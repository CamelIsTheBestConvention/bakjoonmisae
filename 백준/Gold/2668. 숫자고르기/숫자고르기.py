n = int(input())
graph = [[] for i in range(n + 1)]

for i in range(1, n + 1):
  graph[i].append(int(input()))


def dfs(s):
  global result, cnt

  visited[s] = True
  for now in graph[s]:
    if visited[now] == False:
      dfs(now)
    elif visited[now] == True and finished[now] == False:
      if now not in result:
        cnt += 1
        result.append(now)
        return
    else:
      return
  finished[s] = True


result = []
cnt = 0

for i in range(1, n + 1):
  visited = [False] * (n + 1)
  finished = [False] * (n + 1)
  dfs(i)

result.sort()
print(cnt)
for i in result:
  print(i)