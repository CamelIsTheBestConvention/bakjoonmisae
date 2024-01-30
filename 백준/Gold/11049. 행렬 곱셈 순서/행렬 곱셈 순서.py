import sys

def hanggop():
    n = int(sys.stdin.readline())
    hangyeol = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
    table = [[0]*n for _ in range(n)]
    INF = int(1e9)

    # 행
    for gop in range(1, n):
        for start in range(n - gop):
            end = start + gop
            table[start][end] = float('inf')
            for mid in range(start, end):
                table[start][end] = min(
                    table[start][end],
                    table[start][mid] + table[mid+1][end] 
                    + hangyeol[start][0] * hangyeol[mid][1] * hangyeol[end][1]
                )

    print(table[0][n-1])

hanggop()