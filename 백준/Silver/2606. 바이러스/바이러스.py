import sys

# 컴퓨터 개수와 방문현황, 연결현황을 인자로 받아
def virus(computer, visited, connect):
    # 해당 컴퓨터에 방문 체크
    visited[computer] = True
    
    # 컴퓨터들을 돌며 방문안한 곳이 있으면 재귀
    for i in connect[computer]:
        if not visited[i]:
            virus(i, visited, connect)


# 노드 computer, 간선 network, 방문확인 visited, 연결확인 connect
computer = int(sys.stdin.readline())
network = int(sys.stdin.readline())

visited = [False] * (computer+1)
connect = [[] for _ in range(computer+1)]

# 컴퓨터끼리 연결되게 값 적용
for _ in range(network):
    pc1, pc2 = map(int, sys.stdin.readline().split())
    connect[pc1].append(pc2)
    connect[pc2].append(pc1)

# 1번 컴퓨터를 시작으로 visited값이 True인것을 찾기
virus(1, visited, connect)

# 자기를 제외한 연결되어 감염된 컴퓨터 갯수
print(visited.count(True)-1)