"""
https://leetcode.com/problems/maximum-average-subarray-i

Difficulty: Easy
"""

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        maxAvg =  total / k
        
        for i in range(1, len(nums) - k + 1):
            total = total - nums[i - 1] + nums[i + k - 1]
            maxAvg = max(maxAvg, total / k)

        return maxAvg
    
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        nums.sort()
        print(nums)
        print(nums[-k:])
        return sum(nums[-k:]) / k
    
nums = [1,12,-5,-6,50,3]
k = 4
print(Solution().findMaxAverage(nums, k))

nums = [5]
k = 1
print(Solution().findMaxAverage(nums, k))