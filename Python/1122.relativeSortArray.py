"""
https://leetcode.com/problems/relative-sort-array

Difficulty: Easy
"""

from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        map = {}
        for i in range(len(arr2)):
            map[arr2[i]] = -len(arr2) + i
        arr1.sort(key=lambda x: map[x] if x in map else x)
        
        return arr1
    
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
print(Solution().relativeSortArray(arr1, arr2))

arr1 = [28,6,22,8,44,17]
arr2 = [22,28,8,6]
print(Solution().relativeSortArray(arr1, arr2))

arr1 = [26,21,11,20,50,34,1,18]
arr2 = [21,11,26,20]
print(Solution().relativeSortArray(arr1, arr2))