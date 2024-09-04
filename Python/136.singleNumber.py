from typing import List

"""
https://leetcode.com/problems/single-number/description/

Difficulty: Easy
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = nums[0]

        for i in range(1, len(nums)):
            answer = answer ^ nums[i]

        return answer
    
print(Solution().singleNumber([2,2,1])) # Expected: 1
print(Solution().singleNumber([4,1,2,1,2])) # Expected: 4