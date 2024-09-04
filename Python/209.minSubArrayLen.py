"""
https://leetcode.com/problems/minimum-size-subarray-sum

Difficulty: Medium
"""
from typing import List
    
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        total = 0

        min_len = len(nums) + 1

        while right < len(nums):
            total += nums[right]
            right += 1

            while total >= target:
                min_len = min(min_len, right - left)
                total -= nums[left]
                left += 1

        if min_len == len(nums) + 1:
            return 0
        return min_len

    
    
target = 7
nums = [2,3,1,2,4,3]
print(Solution().minSubArrayLen(target, nums))

target = 4
nums = [1,4,4]
print(Solution().minSubArrayLen(target, nums))

target = 11
nums = [1,1,1,1,1,1,1,1]
print(Solution().minSubArrayLen(target, nums))

target = 15
nums = [1,2,3,4,5]
print(Solution().minSubArrayLen(target, nums))
