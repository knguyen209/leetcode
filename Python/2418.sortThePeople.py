"""
https://leetcode.com/problems/sort-the-people/

Difficulty: Easy
"""

from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        arr = []
        for i in range(len(heights)):
            arr.append((heights[i],i))
        arr.sort(reverse=True)
        answer = []
        for tuple in arr:
            answer.append(names[tuple[1]])
        return answer
    
names = ["Mary","John","Emma"]
heights = [180,165,170]
print(Solution().sortPeople(names, heights))