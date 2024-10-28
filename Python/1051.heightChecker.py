from typing import List

"""
https://leetcode.com/problems/height-checker

Difficulty: Easy
"""

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        arr = heights[:]
        arr.sort()
        answer = 0
        
        for i in range(len(heights)):
            if arr[i] - heights[i] != 0:
                answer += 1

        return answer
    
print(Solution().heightChecker([1,1,4,2,1,3])) # 3