# a : 합을 구해야 하는 정수 n개가 저장되어 있는 리스트
# 정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성

def solve(a):
    ans = 0
    for i in range(len(a)):
        ans += a[i]
    return ans
