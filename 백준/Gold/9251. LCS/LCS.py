import sys

def lcs(x, y):
    m = len(x)
    n = len(y)
    l = [[0]*(n+1) for _ in range(m+1)]
    cnt = 0


    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                l[i][j] = 0
            elif x[i-1] == y[j-1]:
                l[i][j] = l[i-1][j-1]+1
            else:
                l[i][j] = max(l[i-1][j], l[i][j-1])
                cnt = l[i][j]

    return cnt    


first_string = list(sys.stdin.readline())
second_string = list(sys.stdin.readline())

print(lcs(first_string, second_string))