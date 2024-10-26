from typing import List

"""
https://leetcode.com/problems/find-center-of-star-graph
Difficulty: Easy
"""

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return (list(set(edges[1]).intersection(set(edges[0]))))[0]

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        return edges[0][1]
    
edges = [[1,2],[5,1],[1,3],[1,4]]
print(Solution().findCenter(edges))

edges = [[1,2],[2,3],[4,2]]
print(Solution().findCenter(edges))