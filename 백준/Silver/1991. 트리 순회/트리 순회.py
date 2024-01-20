# 이진트리의 노드를 표현하기 위해 데이터를 묶어 사용할 수 있는 클래스를 사용
class Node:
    # 입력된 노드를 초기화
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# 전위순회 - 뿌리를 먼저 방문해 시작
def preOrder(node):
    if node is not None:
        # 현재 노드의 데이터를 출력
        print(node.data, end="")
        # 왼쪽 노드부터 접근해 오른쪽 노드까지 이동
        preOrder(node.left)
        preOrder(node.right)

# 중위순회 - 왼쪽 하위 트리를 방문 후 뿌리 방문
def inOrder(node):
    if node is not None:
        inOrder(node.left)
        print(node.data, end="")
        inOrder(node.right)

# 후위순회 - 하위 트리 모두 방문 후 뿌리 방문
def postOrder(node):
    if node is not None:
        postOrder(node.left)
        postOrder(node.right)
        print(node.data, end="")

# 노드 정보를 저장할 딕셔너리
nodes = {}

N = int(input())
for _ in range(N):
    # 입력값에 현재 노드, 왼쪽 자식, 오른쪽 자식 값 입력
    data, left, right = input().split()

    # 만약 nodes에 입력한 data가 없을 때 
    if data not in nodes:
        # Node(data)를 nodes 딕셔너리에 저장
        nodes[data] = Node(data)
    # 왼쪽 자식노드가 존재할 때
    if left != '.':
        # 근데 그 노드가 아직 생성되지 않았을 때
        if left not in nodes:
            # nodes 딕셔너리의 left자리에 노드를 넣고 그 노드의 왼쪽 자식값으로 넣기
            nodes[left] = Node(left)
            nodes[data].left = nodes[left]
    # 오른쪽 자식노드가 존재할 때
    if right != '.':
        # 근데 그 노드가 아직 생성되지 않았을 때
        if right not in nodes:
            # nodes 딕셔너리의 right자리에 노드를 넣고 그 노드의 오른쪽 자식값으로 넣기
            nodes[right] = Node(right)
            nodes[data].right = nodes[right]

# root에 nodes 딕셔너리에 A값 미리 입력
root = nodes['A']

# 각 순회에 맞는 함수에 시작점인 A노드로 root값 전달
# print("전위 순회: ", end="")
preOrder(root)
print()

# print("중위 순회: ", end="")
inOrder(root)
print()

# print("후위 순회: ", end="")
postOrder(root)
print()
