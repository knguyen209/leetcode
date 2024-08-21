"""
https://leetcode.com/problems/contains-duplicate/

Difficulty: Easy

"""
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) == len(nums)
    
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
            
        return False

    

print(Solution().containsDuplicate([1,2,3,1])) # True

print(Solution().containsDuplicate([1,2,3,4])) # False

print(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2])) # True