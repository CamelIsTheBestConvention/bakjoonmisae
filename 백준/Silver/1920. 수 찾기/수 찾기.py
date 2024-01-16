# 어차피 입력값 쪼개야해서 n값을 왜 받는진 모르겠지만 횟수 받기
n = int(input())
# n값만큼 받아서 쪼개 리스트에 저장하고 오름차수 정렬
arr = list(map(int, input().split()))
arr.sort()

# 찾을 데이터의 갯수 입력
n2 = int(input())
# n값만큼 받아서 쪼개 리스트에 저장
arr2 = list(map(int, input().split()))

# 이분 탐색으로 찾기
def binary_search(target, data):
    # 시작 과 끝 위치를 잡는다
    start = 0 
    end = len(data) - 1 

    # 시작에서 끝으로 가는동안 중간 값을 지정
    while start <= end:
        mid = (start + end) // 2

        # 찾고자 하는 값이 목록에 있으면 1을 리턴
        if data[mid] == target:
            return 1

        # 검색값이 중간값보다 작으면 중간값부터 끝까지 날리기
        elif data[mid] > target: 
            end = mid - 1
        # 검색값이 중간값보다 크면 처음부터 중간값까지 날리기
        else:              
            start = mid + 1
    # 목록에 없으면 0을 반환
    return 0

# 찾고자하는 수만큼 함수를 돌리고 그 값의 유무를 판단해 1 0 출력
for i in arr2:
    print(binary_search(i, arr))