"""
https://leetcode.com/problems/two-sum
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums) - 1):
            remainder = target - nums[i]
            for j in range(i+1,len(nums)):
                if nums[j] == remainder:
                    return [i, j]
        return []

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(0,len(nums)):
            if target - nums[i] in map:
                return [map[target - nums[i]], i]
            else:
                map[nums[i]] = i
        return []
    
print(Solution().twoSum([2,7,11,15], 9))
print(Solution().twoSum([3,2,4], 6))
print(Solution().twoSum([3,3], 6))