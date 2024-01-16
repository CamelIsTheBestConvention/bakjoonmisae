n = int(input())
arr = list(map(int, input().split()))
arr.sort()

n2 = int(input())
arr2 = list(map(int, input().split()))

def binary_search(target, data):
    start = 0 
    end = len(data) - 1 

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return 1

        elif data[mid] > target: 
            end = mid - 1
        else:              
            start = mid + 1
    return 0

for i in arr2:
    print(binary_search(i, arr))