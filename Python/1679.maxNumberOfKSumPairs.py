"""
https://leetcode.com/problems/max-number-of-k-sum-pairs/

Difficulty: Medium
"""

from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0

        map = {}

        for i in range(len(nums)):
            if nums[i] in map:
                map[nums[i]].append(i)
            else:
                map[nums[i]] = [i]
        
        for i in range(len(nums)):
            target = k - nums[i]
            if target in map and len(map[target]) > 0 and len(map[nums[i]]) > 0:
                if target == nums[i] and len(map[target]) < 2:
                    continue

                map[target].pop()
                map[nums[i]].pop()
                count += 1
                
        return count
    
nums = [1,2,3,4]
k = 5
print(Solution().maxOperations(nums, k)) # 2: (1, 4), (2, 3)

nums = [3,1,3,4,3]
k = 6
print(Solution().maxOperations(nums, k)) # 1: (3, 3)