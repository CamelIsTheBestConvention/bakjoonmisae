n = int(input())
arr = list(map(int, input().split()))
result = 0

for i in range(3) :
    if arr[i] <= n :
        result += arr[i]
    else :
        result += n

print(result)