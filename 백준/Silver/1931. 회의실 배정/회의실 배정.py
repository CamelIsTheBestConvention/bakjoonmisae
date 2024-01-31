import sys
input = sys.stdin.readline

def set_meeting():
    n = int(input())
    meeting = [list(map(int, input().split())) for _ in range(n)]
    meeting.sort(reverse=False, key=lambda x:(x[1], x[0]))
    cnt = 1
    reserve = 0

    while reserve <= n:
        for j in range(reserve+1, n+1):
            if j == n:
                return cnt
            elif meeting[reserve][1] <= meeting[j][0]:
                cnt = cnt + 1
                reserve = j
                break

    return cnt


print(set_meeting())