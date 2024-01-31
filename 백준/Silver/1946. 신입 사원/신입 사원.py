import sys
input = sys.stdin.readline

def employ():
    t = int(input())

    for _ in range(t):
        n = int(input())
        new_comer = [list(map(int, input().split())) for _ in range(n)]
        new_comer.sort(key=lambda x:x[0])

        max_interview_rank = new_comer[0][1]
        cnt = 1

        for i in range(1, n):
            if new_comer[i][1] < max_interview_rank:
                cnt += 1
                max_interview_rank = new_comer[i][1]
                
        print(cnt)

employ()
