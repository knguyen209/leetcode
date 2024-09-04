from typing import List

"""
https://leetcode.com/problems/insert-interval

Difficulty: Medium
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        answer = []
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])

        answer.append(intervals[0])

        for i in range(1, len(intervals)):
            last = answer[-1]
            if last[1] >= intervals[i][0] and last[1] >= intervals[i][1]:
                continue
            elif last[1] >= intervals[i][0] and last[1] <= intervals[i][1]:
                answer[-1] = [last[0], intervals[i][1]]
            else:
                answer.append(intervals[i])    

        return answer
    
intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(Solution().insert(intervals, newInterval))
# Expected: [[1,5],[6,9]]