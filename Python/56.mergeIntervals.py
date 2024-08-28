from typing import List

"""
https://leetcode.com/problems/merge-intervals

Difficulty: Medium
"""

# O(n^2)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        is_merged = [False for _ in range(len(intervals))]
        intervals.sort(key=lambda x: x[0])
        answer = []
        
        for i in range(len(intervals)):
            if is_merged[i] == False:
                [start, end] = intervals[i]
                
                for j in range(i, len(intervals)):
                    if is_merged[j] == False and end >= intervals[j][0] and end <= intervals[j][1]:
                        end = intervals[j][1]
                        is_merged[j] = True
                    
                    if is_merged[j] == False and start <= intervals[j][0] and end >= intervals[j][1]:
                        is_merged[j] = True
                        
                answer.append([start,end])

        return answer
    
# O(n)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer = []
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

print(Solution().merge([[0,2],[1,4],[3,5],[7,9]]))
# Expected: [[0,5], [7,9]]
print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
# Expected: [[1,6],[8,10],[15,18]]

print(Solution().merge([[1,4],[4,5]]))
# # Expected: [[1,5]]

print(Solution().merge([[1,4],[0,4]]))
# # Expected: [[0,4]]

print(Solution().merge([[1,4],[2,3]]))
# # Expected: [[0,4]]

