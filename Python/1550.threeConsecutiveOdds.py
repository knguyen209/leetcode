from typing import List

"""
https://leetcode.com/problems/three-consecutive-odds
Difficulty: Easy
"""

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for num in arr:
            if num % 2 != 0:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0

        return False