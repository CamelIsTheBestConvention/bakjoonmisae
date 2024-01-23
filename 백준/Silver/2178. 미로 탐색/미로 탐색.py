# [0,0]에서 [n,m]으로 이동할 때 지나야하는 최소 칸 수 미로찾기
from collections import deque

# 상하 movex, 좌우 movey를 지정. 이동할때 좌표 변화
movex = [-1, 1, 0, 0]
movey = [0, 0, -1, 1]

# x좌표와 y좌표를 받는 미로 찾기 함수
def maze_runner(x, y):
    # 데큐를 사용하고 현재 좌표 추가 (0, 0)
    queue = deque()
    queue.append((x, y))

    # 큐가 없을 때까지 반복. 큐값에서 처음 들어온값을 pop해 x, y에 저장
    while queue:
        x, y = queue.popleft()

        # 상하좌우를 확인해야 해서 4번 반복하고 nx, ny값에 담는다.(좌표갱신)
        for i in range(4):
            nx = x + movex[i]
            ny = y + movey[i]

            # 만약 nx가 0보다 작거나 n보다 크거나 같을 때
            # ny가 0보다 작거나 m보다 크거나 같을 때
            # 즉 갱신한 좌표가 미로를 안 벗어났는지 확인
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 새로운 좌표가 벽이면 다음 방향으로 넘어간다.(지나가는 길은 1이기 때문)
            if maze[nx][ny] == 0:
                continue

            # 새로운 좌표로 이동가능하면 현재위치에서 이동하고 칸 수를 기록한 뒤 좌 큐에 저장
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

    # 현재 위치의 이동칸 반환
    return maze[n - 1][m - 1]

# 행 n, 열 m을 입력받기
# n, m = map(int, sys.stdin.readline().split())
n, m = map(int, input().split())

# 미로 변수를 만들고 다음 미로 값을 입력받음
maze = []
for i in range(n):
    maze.append(list(map(int, input())))

print(maze_runner(0, 0))