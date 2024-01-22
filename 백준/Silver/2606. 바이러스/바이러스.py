import sys


def virus(computer, visited, connect):
    visited[computer] = True
    
    for i in connect[computer]:
        if not visited[i]:
            virus(i, visited, connect)


# 노드 computer, 간선 network, 방문확인 visited, 연결확인 connect
computer = int(sys.stdin.readline())
network = int(sys.stdin.readline())

visited = [False] * (computer+1)
connect = [[] for _ in range(computer+1)]

for _ in range(network):
    pc1, pc2 = map(int, sys.stdin.readline().split())
    connect[pc1].append(pc2)
    connect[pc2].append(pc1)

virus(1, visited, connect)

print(visited.count(True)-1)