"""
https://leetcode.com/problems/find-the-highest-altitude/

Difficulty: Easy
"""

from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        largest = max(0, gain[0])
        for i in range(1, len(gain)):
            gain[i] += gain[i - 1]
            largest = max(largest, gain[i])

        return largest
    
gain = [-5,1,5,0,-7]
print(Solution().largestAltitude(gain))

gain = [-4,-3,-2,-1,4,3,2]
print(Solution().largestAltitude(gain))

gain = [52,-91,72]
print(Solution().largestAltitude(gain))