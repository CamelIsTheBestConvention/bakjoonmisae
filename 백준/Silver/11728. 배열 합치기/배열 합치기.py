import sys
input = sys.stdin.readline

a1, a2 = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr3 = arr1 + arr2
arr3.sort()
print(' '.join(map(str,arr3)))
