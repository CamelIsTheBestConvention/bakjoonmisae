import sys
input = sys.stdin.readline
import heapq

n = int(input())
arr = []

for i in range(n):
    start, end = map(int, input().split())
    arr.append((start, end))
    
arr.sort(key=lambda x: x[0])

heap = []
heapq.heappush(heap, arr[0][1])

for i in range(1, len(arr)):
    if arr[i][0] >= heap[0]:
        heapq.heappop(heap)
        
    heapq.heappush(heap, arr[i][1])
    
print(len(heap))
    
