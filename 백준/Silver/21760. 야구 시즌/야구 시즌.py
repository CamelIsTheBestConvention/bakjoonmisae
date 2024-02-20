import sys
input = sys.stdin.readline

def Baseball_season():
    case = int(input())

    for _ in range(case):
        # 지역리그 n, 팀 m, 지역 리그와 타지역 리그의 비율 k, 전체 경기수 d
        n, m, k, d = list(map(int, input().split()))
        b = 1

        while True:
            a = b * k
            # 같은 지역리그 경기 수+ 다른 지역리그 경기 수
            total_game = ((m*(m-1)//2) * a * n) + (b * m * (m*(n-1)))

            if total_game > d:
                if b == 1:
                    print(-1)
                else:
                    b -= 1
                    a = b * k
                    total_game = ((m*(m-1)//2) * a * n) + (b * m * (m*(n-1)))
                    print(total_game)

                break
            b += 1

Baseball_season()