from typing import List

"""
https://leetcode.com/problems/longest-consecutive-sequence

Difficulty: Medium

Constraint: O(n) Time complexity
"""

# O(nlogn) - Not satisfy the constraint
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums.sort()
        max_length = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                count += 1
                max_length = max(max_length, count)
            elif nums[i] == nums[i - 1]:
                count += 0
            else:
                count = 1

        return max_length
    
nums = [100,4,200,1,3,2]
print(Solution().longestConsecutive(nums)) # Expect: 4

print(Solution().longestConsecutive([1,2,0,1])) # Expect: 3