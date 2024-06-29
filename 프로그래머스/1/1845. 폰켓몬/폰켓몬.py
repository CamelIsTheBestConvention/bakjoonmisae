def solution(nums):
    answer = 0
    
    kind = set(nums)
    many = len(nums) // 2
    answer = min(len(kind), many)
    
    return answer