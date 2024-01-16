n = int(input())
arr = []
result = []

for i in range(n):
    arr.append(int(input()))

for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            continue

for i in arr:
    if i not in result:
        result.append(i)

for i in range(len(result)):
    print(result[i])