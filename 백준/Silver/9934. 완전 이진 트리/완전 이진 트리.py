import sys
input = sys.stdin.read

input_data = input().split()
K = int(input_data[0])
arr = list(map(int, input_data[1:]))
levels = [[] for _ in range(K)]
stack = [(0, len(arr) - 1, 0)]

while stack:
    start, end, level = stack.pop()
    if start > end:
        continue
    
    mid = (start + end) // 2
    levels[level].append(arr[mid])
    
    stack.append((mid + 1, end, level + 1))
    stack.append((start, mid - 1, level + 1))

for level in levels:
    print(' '.join(map(str, level)))
