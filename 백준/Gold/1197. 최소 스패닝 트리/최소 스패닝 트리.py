import sys

# 노드 개수를 입력받아 초기화
def init(n):
    # 부모노드에 자기노드값을 넣기
    parent = [0] * (n + 1)
    for i in range(1, n + 1):
        parent[i] = i
    return parent

# find 함수(루트노드로 받을 parent와 자기노드값 x)
def find(parent, x):
    # 부모 노드 값이 자기 노드랑 다르다면
    if parent[x] != x:
        # find함수를 재귀해서 부모노드와 자기노드가 같을때까지 반복
        parent[x] = find(parent, parent[x])
    # 같을 시 값 반환
    return parent[x]

# union 함수(루트노드 parent와 find함수에서 루트노드를 담을 a, b)
def union(parent, a, b):
    # a와 b에 find에서 받아온 루트 노드값을 입력
    a = find(parent, a)
    b = find(parent, b)
    # 만약 a의 루트노드가 b의 루트노드보다 작을 때
    if a < b:
        # b의 루트노드에 a의 루트노드값을 넣기
        parent[b] = a
    # b의 루트노드가 더 작으면 a에 b를 넣기
    else:
        parent[a] = b

# kruskal 함수(노드의 개수 n과 간선리스트 edges를 저장)
def kruskal(n, edges):
    # 간선리스트를 리스트 안 튜플의 2번 인덱스 값인 가중치를 오름차순으로 정렬
    edges.sort(key=lambda x: x[2])
    # 부모노드에 노드를 저장하는 값을 초기화
    parent = init(n)
    # 가중치 합산 변수 생성
    total_weight = 0


    # 간선리스트를 돌리면서
    for edge in edges:
        # 입력값을 노드a, 노드b, 가중치 변수로 분산 
        a, b, weight = edge
        # a와 b의 루트 노드가 다르다면
        if find(parent, a) != find(parent, b):
            # union 함수를 실행해서 노드를 합치기
            union(parent, a, b)
            # 각각의 가중치를 합쳐서 전체 가중치에 담아 반환
            total_weight += weight

    return total_weight

# 정점, 간선을 첫 입력 때 쪼개서 받고
vertex, line = list(map(int, sys.stdin.readline().split()))
arr = []

# 간선 개수만큼 돌리면서 노드a, 노드b, 가중치weight에 두 번째 값부터 쪼개서 받기
for i in range(line):
    a, b, weight = map(int, sys.stdin.readline().split())
    arr.append((a, b, weight))

# 크루스칼 함수에서 반환되는 합산가중치 출력
print(kruskal(vertex, arr))
