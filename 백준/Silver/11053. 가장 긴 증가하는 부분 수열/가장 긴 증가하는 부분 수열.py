import sys
input = sys.stdin.readline

def longLCS(a):
    # 받은 문자열의 길이를 체크
    length = len(a)
    # 처음 시작을 1로 해야 원소가 처음 나올때 1이 체크된다.
    list = [1]*length

    # 처음껀 비교대상이 없기 때문에 1부터 시작
    for i in range(1, length):
        # i 이전 수들끼리 비교해야 하기 때문에 i까지 반복
        for j in range(i):
            # i값이 j값보다 크고(증가 수열) 리스트에 i를 넣었을 때 기존 리스트보다 길면 갱신
            if a[i] > a[j] and list[i] < list[j]+1:
                list[i] = list[j]+1

    # 리스트에서 제일 최대값을 반환
    return max(list)

n = int(input())
a = list(map(int, input().split()))
print(longLCS(a))