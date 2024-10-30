"""
https://leetcode.com/problems/pascals-triangle-ii

Difficulty: Easy
"""
from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = []
        
        if rowIndex >= 0:
            dp.append(1)
        
        if rowIndex >= 1:
            dp.append(1)

        curr = 2

        while curr <= rowIndex:
            for i in range(len(dp) - 1):
                dp[i] += dp[i + 1]
            dp.insert(0, 1)
            dp[-1] = 1
            curr += 1

        return dp
    
print(Solution().getRow(4))