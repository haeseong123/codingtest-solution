def solution(nums):
    return min(len(set(nums)), len(nums) >> 1)
