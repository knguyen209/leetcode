"""
https://leetcode.com/problems/sort-colors/

Difficulty: Medium
"""

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from collections import Counter
        freq = Counter(nums)
        i = 0
        x = 0
        
        while x <= 2:
            while freq[x] > 0:
                nums[i] = x
                freq[x] -= 1
                i += 1
            x += 1
        

print(Solution().sortColors([2,0,2,1,1,0])) # [0,0,1,1,2,2]