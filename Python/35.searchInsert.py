from typing import List

"""
https://leetcode.com/problems/search-insert-position/

Difficulty: Easy
"""

"""
Given a sorted array of distinct integers and a target value,
return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        mid = (left + right) // 2
        
        if target <= nums[left]:
            return 0
        
        if target > nums[right]:
            return right + 1

        while left + 1 < right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                left = mid
                
            if nums[mid] > target:
                right = mid
        
        if nums[mid] < target:
            return mid + 1

        if nums[mid] > target:
            return mid

        return 0
    
nums = [1,3,5,6]
target = 5
print(Solution().searchInsert(nums, target)) # Expected: 2

# If not, return the index where it would be if it were inserted in order.
nums = [1,3,5,6]
target = 2
print(Solution().searchInsert(nums, target)) # Expected: 1

nums = [1,3,5,6]
target = 7
print(Solution().searchInsert(nums, target)) # Expected: 4

nums = [1,3,5,6]
target = 0
print(Solution().searchInsert(nums, target)) # Expected: 0

nums = [1,3]
target = 3
print(Solution().searchInsert(nums, target))