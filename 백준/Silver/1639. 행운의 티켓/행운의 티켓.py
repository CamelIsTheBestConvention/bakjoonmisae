import sys
input = sys.stdin.readline

def lucky_ticket():
    ticket = input().strip()
    n = len(ticket)
    max_len = 0
    
    for i in range(n):
        for j in range(i+2, n+1, 2):
            mid = (i+j)//2
            left = 0
            right = 0

            for k in range(i, mid):
                left += int(ticket[k])
            for k in range(mid, j):
                right += int(ticket[k])

            if left == right:
                max_len = max(max_len, j-i)

    return max_len

print(lucky_ticket())