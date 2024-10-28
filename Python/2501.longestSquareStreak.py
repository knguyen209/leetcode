"""
https://leetcode.com/problems/longest-square-streak-in-an-array

Difficulty: Medium
"""
from typing import List

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        squares = {}
        nums.sort()
        
        for num in nums:
            squares[num] = num * num

        streak = 0

        for num in nums:
            arr = []
            
            while num in squares:
                arr.append(num)
                num = squares[num]
            
            streak = max(len(arr), streak)

        return streak if streak != 1 else -1 
    
print(Solution().longestSquareStreak([4,3,6,16,8,2])) # 3 [4, 16, 2]
print(Solution().longestSquareStreak([2,3,5,6,7])) # -1