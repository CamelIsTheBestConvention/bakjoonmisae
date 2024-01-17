# n 이 2의7승 중에 입력되고, n x n 의 색종이가 있는데
# 색종이가 다 차있지 않으면 반절로 쪼개면서 채워지는 색종이가 있을때까지 쪼개기

# n x n 값 받기
N = int(input())
# n x n의 종이 값을 받아오기
paper = [list(map(int, input().split())) for _ in range(N)]
# 흰색과 파란색 수를 초기화
white = 0
blue = 0

def cut(x, y, n):
    # 재귀할때마다 초기화되면 안되기 때문에 흰색, 파란색을 전역변수로 가져온다.
    global blue, white
    # 이차원배열에 입력된 x와 y값 넣기(0,0) 부터 시작
    check = paper[x][y]
    # [0][0]부터 [n-1][n-1]까지 완전탐색 하면서
    for i in range(x, x + n):
        for j in range(y, y + n):
            # check값의 색[0][0]이랑 현재 색종이의 색이랑 다르면 재귀를 시작
            # 1/4로 쪼개기 때문에 재귀를 4번 사용해 4분할을 다 검색
            if check != paper[i][j]: 
                cut(x, y, n//2)
                cut(x, y + n//2, n//2)
                cut(x + n//2, y, n//2)
                cut(x + n//2, y + n//2, n//2)
                return

    # 체크값이 0이면 흰색을 1 누적하고, 1이면 파란색을 1 누적한다
    if check == 0: 
        white += 1
        return
    else: 
        blue += 1
        return
# check값을 위해 첫 x, y값을 0,0으로 설정하고 입력값을 길이로 받기 
cut(0, 0, N)
print(white)
print(blue)