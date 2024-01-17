import sys

n = int(sys.stdin.readline())
queue = []
cnt = 0

for i in range(n):
    order = list(map(str, sys.stdin.readline().split()))

    if order[0] == 'push':
        queue.append(order[1])

    if order[0] == 'pop':
        if len(queue)-cnt == 0:
            print('-1')
        else:
            print(queue[cnt])
            cnt += 1

    if order[0] == 'size':
        print(len(queue)-cnt)

    if order[0] == 'empty':
        if len(queue)-cnt == 0:
            print('1')
        else:
            print('0')

    if order[0] == 'front':
        if len(queue)-cnt == 0:
            print('-1')
        else:
            print(queue[cnt])

    if order[0] == 'back':
        if len(queue)-cnt == 0:
            print('-1')
        else:
            print(queue[len(queue)-1])