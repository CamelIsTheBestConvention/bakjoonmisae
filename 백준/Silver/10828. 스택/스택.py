# 스택 기능 구현 문제
# 출력할 명령어의 개수를 입력
import sys
n = int(sys.stdin.readline())
stack = []

# 각 단어가 입력될 때마다 if문 타서 실행
for _ in range(n):
    # 입력이 push일 경우는 값이랑 쪼개져서 인덱스 2개로 담기고
    # 그 외의 입력은 1개의 인덱스만 담겨 [0]번째에만 데이터가 있음음
    order = sys.stdin.readline().split()
    # push x일 때 정수 x를 배열에 담는다.
    if order[0] == 'push':
        stack.append(order[1])
    # pop일 때 배열에 가장 뒤에 값을 삭제하고 값을 출력한다
    elif order[0] == 'pop':
        if len(stack) == 0:
            print('-1')
        else:
            print(stack[-1]) 
            del stack[-1] 
    # size일 때 배열에 있는 인덱스의 개수를 출력
    elif order[0] == 'size':
        print(len(stack))
    # empty일 때 배열이 인덱스가 없으면 1, 있으면 0을 출력한다
    elif order[0] == 'empty':
        if len(stack) == 0:
            print('1')
        else:
            print('0')
    # top일 때 배열의 가장 뒤의 값을 출력하고 없으면 -1을 출력
    elif order[0] == 'top':
        if len(stack) == 0:
            print('-1')
        else:
            print(stack[-1])



