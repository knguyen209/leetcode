"""
https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/
Difficulty: Medium
"""

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_num = nums[0]
        max_length = 1
        length = 1

        for i in range(1, len(nums)):
            if nums[i] > max_num:
                max_num = nums[i]
                length = 1
                max_length = 1
                continue

            if nums[i] == max_num:
                length += 1
                max_length = max(length, max_length)
                continue

            if nums[i] < max_num:
                length = 0

        return max_length

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_num = max(nums)
        max_length = 0
        length = 0

        for num in nums:
            if num == max_num:
                length += 1
                max_length = max(length, max_length)
            if num < max_num:
                length = 0

        return max_length
    
print(Solution().longestSubarray([1,2,3,3,2,2])) # 2 [3,3]
print(Solution().longestSubarray([1,2,3,4])) # 1 [4]
# print(Solution().longestSubarray([311155,311155,311155,311155,311155,311155,311155,311155,201191,311155])) # 8
