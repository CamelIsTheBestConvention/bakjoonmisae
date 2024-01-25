
# dfs 함수
def dfs(board, m, n, x, y, visited):
    # nx, ny를 0으로 설정하고
    nx, ny = 0, 0
    # 현재 타일의 방문확인을 true로 변경
    visited[x][y] = True
    
    # 만약 현재 좌표가 -라면 좌우를 확인해야 하기 때문에 y값을 1증가
    if board[x][y] == '-':
        nx = x
        ny = y + 1
    # 좌표가 |라면 상하를 확인해야 하기 때문에 x값을 1증가
    else:
        nx = x + 1
        ny = y
    # 만약 행과 열의 길이만큼 안왔고 타일 값이 같으며 방문하지 않았으면 재귀
    if nx < m and ny < n and board[nx][ny] == board[x][y] and not visited[nx][ny]:
        dfs(board, m, n, nx, ny, visited)

# 타일 입력값 board, 행 m, 열 n
def solution(board, m, n):
    # 타일 개수
    answer = 0
    # 방문확인하기위해 False로 꽉 채우기
    visited = [[False] * n for _ in range(m)]
    # 모든 타일값을 돌면서
    for i in range(m):
        for j in range(n):
            # 만약 현재 좌표가 true라면 건너뛰기
            if visited[i][j]:
                continue
            # dfs 좌표 i, j와 방문확인까지 더해서 재귀한 후 타일 +1 증가
            dfs(board, m, n, i, j, visited)
            answer += 1
    
    return answer
# 열 개수 N, 행 개수 M을 입력받는다.
m, n = map(int, input().split())
# 좌표를 받을 리스트 생성
board = []
# 행 개수만큼 반복해서 타일 입력하기
for _ in range(m):
    row = list(input())
    board.append(row)

print(solution(board, m, n))