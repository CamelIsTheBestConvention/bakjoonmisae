import sys
input = sys.stdin.readline

def pcRoom(n):
    arr = [False] * 100
    people = list(map(int, input().split()))
    count = 0

    for person in people:
        if(arr[person-1] == True):
            count += 1
            continue
        else:
            arr[person-1] = True

    print(count)

n = int(input())

pcRoom(n)