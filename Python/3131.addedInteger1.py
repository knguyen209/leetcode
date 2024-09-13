from typing import List

"""
https://leetcode.com/problems/find-the-integer-added-to-array-i/

Difficulty: Easy
"""

class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return min(nums2) - min(nums1)
    
nums1 = [2,4,6]
nums2 = [5,7,9]
print(Solution().addedInteger(nums1, nums2))
print(Solution().addedInteger([10], [5]))
print(Solution().addedInteger([1,1,1,1], [1,1,1,1]))
