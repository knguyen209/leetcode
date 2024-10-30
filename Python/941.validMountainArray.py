"""
https://leetcode.com/problems/valid-mountain-array/

Difficulty: Easy
"""

from typing import List
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        maxHeight = max(arr)
        maxIndex = arr.index(maxHeight)

        if maxIndex == len(arr) - 1 or maxIndex == 0:
            return False

        leftArr = arr[:maxIndex + 1]
        rightArr = arr[maxIndex:]
        
        for i in range(len(leftArr) - 1):
            if leftArr[i] >= leftArr[i + 1]:
                return False
            
        for i in range(len(rightArr) - 1):
            if rightArr[i] <= rightArr[i + 1]:
                return False
            
        return True
    
print(Solution().validMountainArray([3,5,5]))   # False
print(Solution().validMountainArray([0,3,2,1])) # True