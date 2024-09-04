from typing import List

"""
https://leetcode.com/problems/container-with-most-water/

Difficulty: Medium
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_vol = 0
        
        while left < right:
            vol = min(height[left], height[right]) * (right - left)
            
            if vol >= max_vol:
                max_vol = vol

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1    
            
        return max_vol
    

height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))

height = [1,1]
print(Solution().maxArea(height))