import math

cnt = int(input())
arr = []

nums = list(map(int, input().split()))

for i in range(len(nums)):
    if nums[i] == 1:
        continue
    else:
        for j in range(2, int(math.sqrt(nums[i])) + 1):
            if nums[i] % j == 0:
                break
        else:
            arr.append(nums[i])

print(len(arr))
