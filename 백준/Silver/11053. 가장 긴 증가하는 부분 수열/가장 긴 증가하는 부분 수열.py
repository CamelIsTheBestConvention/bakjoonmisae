import sys
input = sys.stdin.readline

def longLCS(a):
    length = len(a)
    list = [1]*n

    for i in range(1, length):
        for j in range(i):
            if a[i] > a[j] and list[i] < list[j]+1:
                list[i] = list[j]+1

    return max(list)

n = int(input())
a = list(map(int, input().split()))
print(longLCS(a))