import sys

def backpack():
    n, k = map(int, sys.stdin.readline().split())
    items = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    dp = [0 for _ in range(k+1)]
    # 전체 물건을 순회하면서 
    for i in range(n):
        # 가방 무게부터 현재 물건의 무게보다 작은 값까지 -1씩 반복
        for j in range(k, items[i][0]-1, -1):
            # 현재 물건을 배낭에 넣는 것이 가치가 더 크면 넣고
            # 그렇지 않으면 넣지 않는다
            dp[j] = max(dp[j], dp[j-items[i][0]] + items[i][1])

    print(dp[k])

backpack()