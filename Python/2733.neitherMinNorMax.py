"""
https://leetcode.com/problems/neither-minimum-nor-maximum/
Difficulty: Easy
"""

from typing import List

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        minNum = min(nums)
        maxNum = max(nums)

        for num in nums:
            if minNum < num < maxNum:
                return num

        return -1