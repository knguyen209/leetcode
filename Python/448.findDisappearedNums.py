"""
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

Difficulty: Easy
"""
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = set(nums)
        all = set(i for i in range(1, n + 1))
        return list(all.difference(nums))

print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(Solution().findDisappearedNumbers([1,1]))