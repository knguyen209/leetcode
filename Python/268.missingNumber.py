"""
https://leetcode.com/problems/missing-number

Difficulty: Easy
"""
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2
        return total - sum(nums)
    
print(Solution().missingNumber([3, 0, 1]))
print(Solution().missingNumber([0, 1]))