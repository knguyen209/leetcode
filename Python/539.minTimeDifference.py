"""
https://leetcode.com/problems/minimum-time-difference/?envType=daily-question&envId=2024-09-16
Difficulty: Medium
"""

from typing import List


class Solution:

    def findMinDifference(self, timePoints: List[str]) -> int:
        min_diff = 24 * 60
        mins = []
        for timePoint in timePoints:
            arr = timePoint.split(":")
            mins.append(int(arr[0]) * 60 + int(arr[1]))
        
        mins.sort()

        for i in range(1, len(mins)):
            min_diff = min(min_diff, mins[i] - mins[i - 1])

        min_diff = min(min_diff, mins[1] - mins[0])
        min_diff = min(min_diff, mins[0] + 24 * 60 - mins[-1])

        return min_diff
    
timePoints = ["23:59","00:00"]
print(Solution().findMinDifference(timePoints))

timePoints = ["00:00","23:59","00:00"]
print(Solution().findMinDifference(timePoints))

timePoints = ["00:02","23:59","00:03"]
print(Solution().findMinDifference(timePoints))

timePoints = ["01:01","02:01","03:00"]
print(Solution().findMinDifference(timePoints))