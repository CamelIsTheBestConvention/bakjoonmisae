# 몇번 반복할건지 입력 받기
cnt = int(input())
# 입력받은 횟수만큼 반복
for i in range(cnt):
    num = int(input())
    # find라는 배열에 0, 1은 false로 저장하고 뒤에 입력받는 값-1 만큼 True 넣기
    # (0, 1)은 소수가 아니기 때문에 false로 하고 2부터 일단 true로 해놓고 나중에 변경
    find = [False, False] + [True]*(num-1)

    # 2부터 num값의 제곱근을 계산해 +1 붙여주기.
    # int로 변환하면 소숫점을 버리기 때문에 1을 붙여 값이 더 높음을 인지
    for j in range(2, int(num ** (1/2)) + 1):
        # 만약 find 배열의 j번쨰가 true일 때
        if find[j]:
            # j가 2이면 2의 2배수부터 입력값미만이라 +1까지 2씩 증가하며 반복
            for k in range(j*2, num+1, j):
                # 배수씩 뛰는거라 2이면 4, 6, 8... 등이 false로 바뀜
                find[k] = False
    # 변수 두개에 입력값의 반절씩 넣기
    # 가운데서 좌우로 이동하며 값을 찾기 위함
    left = right = num // 2

    # 왼쪽으로 갈 값이 0보다 클 때
    while left > 0:
        # 만약 find의 [left], [right]가 true이면 left, right를 출력하고 빠져나오기
        if find[left] and find[right]:
            print(left, right)
            break
        # false라면 left는 1 빼고 right는 1 더하고 left가 0이 될떄까지 무한 반복
        else:
            left -= 1
            right += 1