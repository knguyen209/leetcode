"""
https://leetcode.com/problems/find-pivot-index

Difficulty: Easy
"""
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)

        for i in range(len(nums)):
            right -= nums[i]

            if left == right:
                return i
            
            left += nums[i]

        return -1
            
    
nums = [1,7,3,6,5,6]
print(Solution().pivotIndex(nums))

nums = [1,2,3]
print(Solution().pivotIndex(nums))

nums = [2,1,-1]
print(Solution().pivotIndex(nums))